from .example_documents import example_documents, example_news
from timeline.models import Document

# Simulate that half the documents are news and the other half are comments
def select_example_documents(document_types, documents=example_documents):
    # If we ask for both types of documents, it return all of them
    if document_types == "both":
        return documents

    half = int(len(example_documents)/2)
    if document_types == "news":
        # If we ask for news documents, returns the first half of the list
        return documents[:half]
    else:
        # If we want comments documents, returns the second half of the list
        return documents[half:]

def mock_document(content, is_news):
    doc, created = Document.objects.get_or_create(content=content, is_news=is_news, date=example_news["date"], author=example_news["author"])
    if created: doc.save()
    return doc

def mock_documents():
    # Mock half the documents as news
    news_documents = select_example_documents(document_types="news")
    for content in news_documents:
        mock_document(content, is_news=True)
    # Mock half the documents as comments
    comments_documents = select_example_documents(document_types="comments")
    for content in comments_documents:
        mock_document(content, is_news=False)
