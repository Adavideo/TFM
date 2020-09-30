from timeline.models import Document
from .example_documents import *


def mock_document(content=example_documents[0], is_news=True):
    doc, created = Document.objects.get_or_create(is_news=is_news, content=content, author=example_author, date=example_date)
    if created: doc.save()
    return doc

def mock_news(number=0):
    news = mock_document(content=news_content[number], is_news=True)
    return news

def mock_documents_list(content_list=news_content, is_news=True):
    list = [ mock_document(content=content, is_news=is_news) for content in content_list]
    return list

def mock_news_list():
    news_list = mock_documents_list(news_content, is_news=True)
    return news_list

def mock_comments():
    comments_list = mock_documents_list(comments_content, is_news=False)
    return comments_list

def mock_news_and_comments():
    documents_list = mock_news_list()
    documents_list.extend( mock_comments() )
    return documents_list

def mock_documents():
    return mock_documents_list()
