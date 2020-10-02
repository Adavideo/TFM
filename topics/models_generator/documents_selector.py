from config import default_documents_limit
from timeline.models import Document


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

def get_documents_content(documents_list):
    documents_content = []
    for doc in documents_list:
        documents_content.append(doc.content)
    return documents_content

def select_documents_from_database(document_types, max_num_documents=default_documents_limit):
    with_news, with_comments = short_document_types(document_types)
    if with_news and with_comments:
        print("Getting all documents from database")
        documents_list = Document.objects.all()[:max_num_documents]
    else:
        print("Getting "+document_types+" documents from database")
        documents_list = Document.objects.filter(is_news=with_news)[:max_num_documents]
    return documents_list

def select_documents(document_types, max_num_documents):
    documents_list = select_documents_from_database(document_types, max_num_documents)
    documents_content = get_documents_content(documents_list)
    return documents_content
