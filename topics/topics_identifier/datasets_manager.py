from sklearn.datasets.base import Bunch


def generate_dataset(documents):
    dataset = Bunch()
    dataset['data'] = documents
    return dataset

def generate_dataset_from_threads(threads_list):
    documents = []
    for thread in threads_list:
        thread_documents = thread.documents_content()
        documents.extend(thread_documents)
    dataset = generate_dataset(documents)
    return dataset
