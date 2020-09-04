from django.db import models
from timeline.models import Document, Topic
from .config import *


class Tree(models.Model):
    name = models.CharField(max_length=tree_name_max_length, unique=True)
    news = models.BooleanField(default=False)
    comments = models.BooleanField(default=False)

    def get_cluster(self, cluster_number, level):
        cluster, cleated = Cluster.objects.get_or_create(tree=self, number=cluster_number, level=level)
        return cluster

    def get_clusters_of_level(self, level):
        clusters = Cluster.objects.filter(tree=self, level=level)
        return clusters

    def add_clusters(self, level, clusters_list):
        for cluster in clusters_list:
            cluster.tree = self
            cluster.level = level
            cluster.save()

    def get_reference_documents(self, level):
        clusters_list = self.get_clusters_of_level(level)
        reference_documents = []
        for cluster in clusters_list:
            reference_documents.append(cluster.reference_document)
        return reference_documents

    def add_reference_documents(self, level, reference_documents):
        clusters = self.get_clusters_of_level(level)
        for i in range(len(clusters)):
            clusters[i].assign_reference_document(content=reference_documents[i])


    # Links the children clusters on the inferior level (level-1) to their parent cluster on the provided level.
    # Parent clusters are the ones that include the reference document of the children cluster.
    def link_children_to_parents(self, parents_level):
        parent_clusters = Cluster.objects.filter(tree=self, level=parents_level)
        for parent in parent_clusters:
            children = parent.children()
            for child_cluster in children:
                child_cluster.parent = parent
                child_cluster.save()

    def add_documents_to_cluster(self, level, cluster_number, cluster_documents):
        for document_content in cluster_documents:
            cluster = self.get_cluster(cluster_number, level)
            cluster.add_document(content=document_content)
        if level > 0:
            self.link_children_to_parents(level)

    def add_documents_to_several_clusters(self, level, clusters_list):
        for num_cluster in range(len(clusters_list)):
            cluster_documents = clusters_list[num_cluster]
            self.add_documents_to_cluster(level, num_cluster, cluster_documents)

    def __str__(self):
        text = "Tree "+ self.name + " - documents: "
        if self.news: text += "news"
        if self.news and self.comments: text += " and "
        if self.comments: text += "comments"
        return text


class Cluster(models.Model):
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, null=True)
    number = models.IntegerField()
    level = models.IntegerField(null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    reference_document = models.CharField(max_length=reference_documents_max_length, null=True)
    terms = models.CharField(max_length=terms_max_length)

    def get_terms(self):
        cleaned_terms_string = self.terms.strip("[]").replace(" ", "").replace("'","")
        terms_list = cleaned_terms_string.split(",")
        return terms_list

    def assign_reference_document(self, content):
        check_max_length("Reference document", content)
        self.reference_document = content
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
            children_search = Cluster.objects.filter(tree=self.tree, level=self.level-1, reference_document=doc.content)
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
        text = "Cluster - tree "+ self.tree.name
        text += ", level " + str(self.level) + ", num cluster "+str(self.number)
        return text


class ClusterDocument(models.Model):
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)

    def __str__(self):
        text = str(self.cluster)+" - "+str(self.document)
        return text
