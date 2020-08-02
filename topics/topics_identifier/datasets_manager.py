from sklearn.datasets.base import Bunch
from .models import Document


def select_documents_level0(news, comments):
    documents = []
    if news and comments:
        documents_list = Document.objects.all()
    else:
        documents_list = Document.objects.filter(news=news)
    
    for doc in documents_list:
        documents.append(doc.content)
    return documents

def generate_dataset(level, tree):
    if level == 0:
        documents = select_documents_level0(tree.news, tree.comments)
    else:
        # Gets the reference documents of the inferior level
        documents = tree.get_reference_documents(level-1)
    dataset = Bunch()
    dataset['data'] = documents
    return dataset
