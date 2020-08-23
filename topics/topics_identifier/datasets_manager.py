from sklearn.datasets.base import Bunch
from .documents_selector import select_documents


def generate_dataset(documents):
    dataset = Bunch()
    dataset['data'] = documents
    return dataset

def get_dataset(tree, level=0, documents_options=None):
    if level == 0:
        documents = select_documents(documents_options)
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
