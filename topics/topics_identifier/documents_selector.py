from .models import Document
from config import batch_size


def short_document_types(document_types):
    if document_types == "both":
        news = True
        comments = True
    elif document_types == "news":
        news = True
        comments = False
    else:
        news = False
        comments = True
    return news, comments

def check_document_types(documents_options):
    document_types = documents_options["types"]
    print("Selecting "+documents_options["types"]+" type of documents")
    with_news, with_comments = short_document_types(documents_options["types"])
    return with_news, with_comments

def select_documents_from_database(documents_options):
    with_news, with_comments = check_document_types(documents_options)
    if with_news and with_comments:
        documents_list = Document.objects.all()
    else:
        documents_list = Document.objects.filter(is_news=with_news)
    return documents_list

def get_number_of_documents(documents_options):
    documents = select_documents_from_database(documents_options)
    return len(documents)

def get_documents_content(documents_list):
    documents_content = []
    for doc in documents_list:
        documents_content.append(doc.content)
    return documents_content

def get_documents_batch(document_list, batch_options):
    end = batch_options["size"] * batch_options["number"]
    start = end - batch_options["size"]
    batch = document_list[start:end]
    return batch

def select_documents(documents_options, batch_options=None):
    all_documents = select_documents_from_database(documents_options)
    if batch_options:
        documents_batch = get_documents_batch(all_documents, batch_options)
    else:
        documents_batch = all_documents
    documents_content = get_documents_content(documents_batch)
    return documents_content

def get_documents_from_threads(threads_list):
    documents = []
    for thread in threads_list:
        thread_documents = thread.documents_content()
        documents.extend(thread_documents)
    return documents
