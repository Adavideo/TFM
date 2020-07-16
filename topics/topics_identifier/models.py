from django.db import models

class Document(models.Model):
    content = models.CharField(max_length=41000) # max length news 40921, comments 19996

    def __str__(self):
        text = "Document "+str(self.id)
        return text

class Cluster(models.Model):
    dataset = models.CharField(max_length=25)
    number = models.IntegerField()
    level = models.IntegerField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    reference_document = models.ForeignKey(Document, on_delete=models.SET_NULL, null=True)
    terms = models.CharField(max_length=255)

    def assign_reference_document(self, content):
        doc, created = Document.objects.get_or_create(content=content)
        self.reference_document = doc
        self.save()

    def add_document(self, content):
        doc, created = Document.objects.get_or_create(content=content)
        ClusterDocument.objects.get_or_create(cluster=self, document=doc)

    def documents(self):
        documents = []
        for cluster_document in ClusterDocument.objects.filter(cluster=self):
            documents.append(cluster_document.document)
        return documents

    def children(self):
        # Level 0 is the lowest level. Does not have children.
        if self.level == 0:
            return []
        # Search clusters that has this cluster assigned as parent
        children = Cluster.objects.filter(parent=self)
        if not children:
            # Search clusters in the inferior level that has one of the document of this cluster as reference document
            children = []
            for doc in self.documents():
                children_search = Cluster.objects.filter(dataset=self.dataset, level=self.level-1, reference_document=doc)
                children.extend(children_search)
        return children

    def __str__(self):
        text = "Dataset "+self.dataset+" - level " + str(self.level) + " cluster "+str(self.number)
        return text

class ClusterDocument(models.Model):
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)

    def __str__(self):
        text = str(self.cluster)+" - "+str(self.document)
        return text
