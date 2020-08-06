from sklearn.datasets.base import Bunch
from .models import Document


def select_documents_level0(news, comments):
    documents = []
    if news and comments:
        documents_list = Document.objects.all()
    else:
        documents_list = Document.objects.filter(is_news=news)

    for doc in documents_list:
        documents.append(doc.content)
    return documents

def generate_dataset(documents):
    dataset = Bunch()
    dataset['data'] = documents
    return dataset

def get_dataset(tree, level=0):
    if level == 0:
        documents = select_documents_level0(tree.news, tree.comments)
    else:
        # Gets the reference documents of the inferior level
        documents = tree.get_reference_documents(level-1)
    dataset = generate_dataset(documents)
    return dataset

def generate_dataset_from_threads(threads_list):
    documents = []
    for thread in threads_list:
        thread_documents = thread.documents_content()
        documents.extend(thread_documents)
    dataset = generate_dataset(documents)
    return dataset
