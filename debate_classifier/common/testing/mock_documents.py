from timeline.models import Document
from .example_documents import *
from .example_threads import news_titles, news_uris


def mock_document(content=example_documents[0], is_news=True):
    doc, created = Document.objects.get_or_create(is_news=is_news, content=content, author=example_author, date=example_date)
    if created: doc.save()
    return doc

def mock_news(number=0):
    news = mock_document(content=news_content[number], is_news=True)
    thread_info = { "thread_number":number, "title":news_titles[number], "uri":news_uris[number] }
    news.assign_thread(thread_info)
    return news

def mock_documents(content_list=[], is_news=True):
    if not content_list:
        if is_news:
            content_list = news_content
        else: content_list = comments_content
    documents = [ mock_document(content, is_news) for content in content_list]
    return documents

def mock_news_list():
    news_list = [ mock_news(number=i) for i in range(len(news_content)) ]
    return news_list

def mock_comments(content_list=comments_content):
    comments_list = [ mock_document(content=content, is_news=False) for content in content_list ]
    return comments_list

def mock_news_and_comments():
    documents_list = mock_news_list()
    documents_list.extend( mock_comments() )
    return documents_list

def ensure_documents(news, comments):
    if not Document.objects.all():
        if news: mock_news_list()
        if comments: mock_comments()
