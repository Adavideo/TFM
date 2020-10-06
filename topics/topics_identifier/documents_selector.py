from config import batch_size
from .models import Document
from .batches_util import get_batch_limits


def get_number_of_documents(documents_types):
    if documents_types == "both":
        num_documents = len(Document.objects.all())
    else:
        is_news = (documents_types == "news")
        num_documents = len(Document.objects.filter(is_news=is_news))
    return num_documents

def select_documents(documents_types, batch_number, size=batch_size):
    start, end = get_batch_limits(batch_number, size)
    if documents_types == "both":
        documents_list = Document.objects.all()[start:end]
    else:
        is_news = (documents_types == "news")
        documents_list = Document.objects.filter(is_news=is_news)[start:end]
    documents_content = [ doc.content for doc in documents_list ]
    return documents_content
