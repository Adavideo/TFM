from timeline.models import Thread
from .mock_documents import mock_news, mock_comments, mock_document


def mock_thread(thread_number, with_documents=False, news_number=None):
    if not news_number: news_number = thread_number
    if not with_documents:
        thread = Thread(number=thread_number)
        thread.save()
    else:
        news = mock_news(number=news_number)
        thread = news.thread
        # Assign comments
        start = news_number*2
        end = start+2
        comments_list = mock_comments()[start:end]
        for comment in comments_list:
            comment.thread = thread
            comment.save()
    return thread

def mock_threads_list(num_threads=2):
    return [ mock_thread(thread_number=n, with_documents=True) for n in range(num_threads)]


def mock_threads_with_topic(topic):
    topic.save()
    thread_list = mock_threads_list()
    topic.assign_threads_list(thread_list)
    return thread_list

def mock_thread_with_news(title, content, thread_number=0):
    thread = Thread(number=thread_number, title=title)
    thread.save()
    news = mock_document(content=title+"\n"+content, is_news=True)
    news.thread = thread
    news.save()
    return thread
