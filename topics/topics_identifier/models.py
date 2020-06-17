from django.db import models

class Document(models.Model):
    content = models.CharField(max_length=41000) # max length news 40921, comments 19996

    def __str__(self):
        text = "Document "+str(self.id)
        return text

def find_or_create_document(content):
    doc_search = Document.objects.filter(content=content)
    if doc_search:
        doc = doc_search[0]
    else:
        doc = Document(content=content)
        doc.save()
    return doc

class Cluster(models.Model):
    dataset = models.CharField(max_length=25)
    number = models.IntegerField()
    reference_document = models.ForeignKey(Document, on_delete=models.SET_NULL, null=True)
    terms = models.CharField(max_length=255)

    def assign_reference_document(self, content):
        doc = find_or_create_document(content)
        self.reference_document = doc
        self.save()

    def add_document(self, content):
        doc = find_or_create_document(content)
        cluster_search = ClusterDocument.objects.filter(cluster=self, document=doc)
        if not cluster_search:
            cluster_document = ClusterDocument(cluster=self, document=doc)
            cluster_document.save()

    def documents(self):
        documents = []
        for cluster_document in ClusterDocument.objects.filter(cluster=self):
            documents.append(cluster_document.document)
        return documents

    def __str__(self):
        text = "Dataset "+self.dataset+" Cluster "+str(self.number)
        return text

class ClusterDocument(models.Model):
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)

    def __str__(self):
        text = str(self.cluster)+" - "+str(self.document)
        return text
