from .models import Document
from .config import default_document_limit


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

def ensure_documents_limit(documents, limit=default_document_limit):
    # Cutting to the maximum number of documents, to not overload the aviable memory.
    num_documents = len(documents)
    print("Documents selected: "+str(num_documents))
    if num_documents > limit:
        print("Adjusting to limit of "+str(limit)+" documents")
        documents = documents[:limit]
    return documents

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

def get_documents_content(documents_list):
    documents_content = []
    for doc in documents_list:
        documents_content.append(doc.content)
    return documents_content

def select_documents(documents_options, limit=default_document_limit, topic=None):
    documents_list = select_documents_from_database(documents_options)
    documents_list = ensure_documents_limit(documents_list, limit)
    documents_content = get_documents_content(documents_list)
    return documents_content
