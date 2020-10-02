from timeline.models import Thread
from .example_threads import news_titles, news_uris
from .mock_documents import mock_news, mock_comments


def mock_thread(thread_number, with_documents=False, news_number=0):
    if not with_documents:
        thread = Thread(number=thread_number)
        thread.save()
    else:
        news = mock_news(number=news_number)
        # Assign news
        thread_info = { "thread_number":thread_number, "title":news_titles[news_number], "uri":news_uris[news_number]}
        news.assign_thread(thread_info)
        thread = news.thread
        # Assign comments
        start = news_number*2
        end = start+2
        comments_list = mock_comments()[start:end]
        for comment in comments_list:
            comment.assign_thread(thread_info)
    return thread

def mock_threads_list():
    thread0 = mock_thread(thread_number=0, with_documents=True, news_number=0)
    thread1 = mock_thread(thread_number=1, with_documents=True, news_number=1)
    return [thread0, thread1]

def mock_threads_with_topic(topic):
    topic.save()
    thread_list = mock_threads_list()
    topic.assign_threads_list(thread_list)
    return thread_list
