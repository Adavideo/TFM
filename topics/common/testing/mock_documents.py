from timeline.models import Document
from .example_documents import *


def mock_document(content=comments_content[0], is_news=False):
    doc, created = Document.objects.get_or_create(is_news=is_news, content=content, author=example_author, date=example_date)
    if created: doc.save()
    return doc

def mock_news(number=0):
    news = mock_document(content=news_content[number], is_news=True)
    return news

def mock_comments():
    comments = []
    for content in comments_content:
        doc = mock_document(content=content, is_news=False)
        comments.append(doc)
    return comments

def mock_news_and_comments():
    mock_news(number=0)
    mock_news(number=1)
    mock_comments()

def mock_documents():
    return mock_comments()
