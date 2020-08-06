from timeline.models import Thread
from .example_threads import news_titles, news_uris
from .mock_documents import mock_news, mock_comments


def mock_thread(thread_number, with_documents=False, news_number=0):
    thread = Thread(number=thread_number)
    thread.save()
    if with_documents:
        news = mock_news(number=news_number)
        # Assign news
        thread_info = { "thread_number":thread_number, "title":news_titles[news_number], "uri":news_uris[news_number]}
        news.assign_thread(thread_info)
        # Assign comments
        comments_list = mock_comments()[:5]
        for comment in comments_list:
            comment.assign_thread(thread_info)
    return thread
