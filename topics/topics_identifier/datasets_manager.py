from sklearn.datasets.base import Bunch
from .models import Cluster, Document

def select_documents():
    documents = []
    documents_list = Document.objects.all()
    for doc in documents_list:
        documents.append(doc.content)
    return documents

def get_reference_documents(tree_name, level):
    all_clusters = Cluster.objects.filter(dataset=tree_name, level=level)
    reference_documents = []
    for cluster in all_clusters:
        reference_documents.append(cluster.reference_document.content)
    return reference_documents

def generate_dataset(level, tree_name=""):
    dataset = Bunch()
    if level == 0:
        documents = select_documents()
    else:
        # Gets the reference documents of the inferior level
        documents = get_reference_documents(tree_name, level-1)
    dataset['data'] = documents
    return dataset
