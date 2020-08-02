from django.db import models


class Tree(models.Model):
    name = models.CharField(max_length=25, unique=True)
    news = models.BooleanField(default=False)
    comments = models.BooleanField(default=False)

    def get_cluster(self, cluster_number, level):
        cluster, cleated = Cluster.objects.get_or_create(tree=self, number=cluster_number, level=level)
        return cluster

    def get_clusters_of_level(self, level):
        clusters = Cluster.objects.filter(tree=self, level=level)
        return clusters

    def get_reference_documents(self, level):
        clusters_list = self.get_clusters_of_level(level)
        reference_documents = []
        for cluster in clusters_list:
            reference_documents.append(cluster.reference_document.content)
        return reference_documents

    def add_clusters(self, level, clusters_information):
        num_clusters = len(clusters_information["terms"])
        for cluster_index in range(0, num_clusters):
            cluster = self.get_cluster(cluster_index, level)
            cluster.terms = clusters_information["terms"][cluster_index]
            reference_document = clusters_information["reference_documents"][cluster_index]
            cluster.assign_reference_document(content=reference_document)
            cluster.save()

    # Links the children clusters on the inferior level (level-1) to their parent cluster on the provided level.
    # Parent clusters are the ones that include the reference document of the children cluster.
    def link_children_to_parents(self, parents_level):
        parent_clusters = Cluster.objects.filter(tree=self, level=parents_level)
        for parent in parent_clusters:
            children = parent.children()
            for child_cluster in children:
                child_cluster.parent = parent
                child_cluster.save()

    def add_documents_to_clusters(self, level, documents_clusters_list):
        for doc_cluster in documents_clusters_list:
            cluster_number = doc_cluster["cluster_number"]
            cluster = self.get_cluster(cluster_number, level)
            document = doc_cluster["document"]
            cluster.add_document(content=document)
        if level > 0:
            self.link_children_to_parents(level)

    def __str__(self):
        text = "Tree "+ self.name + " - documents: "
        if news:
            text += "news"
        if news and comments:
            text += " and"
        if comments:
            text += "comments"
        return text


class Document(models.Model):
    content = models.CharField(max_length=41000, unique=True) # max length news 40921, comments 19996
    is_news = models.BooleanField(null=False)

    def __str__(self):
        text = "Document "+ str(self.id) + " - "
        if self.is_news:
            text += "type news, "
        else:
            text += "type comment, "
        text += "content: "+ self.content
        return text


class Cluster(models.Model):
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, null=False)
    number = models.IntegerField()
    level = models.IntegerField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    reference_document = models.ForeignKey(Document, on_delete=models.SET_NULL, null=True)
    terms = models.CharField(max_length=255)

    def assign_reference_document(self, content):
        doc = Document.objects.get(content=content)
        self.reference_document = doc
        self.save()

    def add_document(self, content):
        doc = Document.objects.get(content=content)
        ClusterDocument.objects.get_or_create(cluster=self, document=doc)

    def documents(self):
        documents = []
        for cluster_document in ClusterDocument.objects.filter(cluster=self):
            documents.append(cluster_document.document)
        return documents

    # Search for clusters in the inferior level that have a document of this cluster as reference document
    def find_children_by_reference_document(self):
        children = []
        for doc in self.documents():
            children_search = Cluster.objects.filter(tree=self.tree, level=self.level-1, reference_document=doc)
            children.extend(children_search)
        return children

    def children(self):
        # Level 0 is the lowest level. Does not have children.
        if self.level == 0:
            return []
        # Search clusters that has this cluster assigned as parent
        children = Cluster.objects.filter(parent=self)
        if not children:
            children = self.find_children_by_reference_document()
        return children

    def __str__(self):
        text = "Cluster - tree "+ self.tree.name+", level " + str(self.level) + ", num cluster "+str(self.number)
        return text


class ClusterDocument(models.Model):
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)

    def __str__(self):
        text = str(self.cluster)+" - "+str(self.document)
        return text
