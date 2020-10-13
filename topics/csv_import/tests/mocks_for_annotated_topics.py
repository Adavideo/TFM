from timeline.models import Thread
from .mocks import mock_document, mock_topic


def mock_thread_with_news(title, content, thread_number=0):
    thread = Thread(number=thread_number, title=title)
    thread.save()
    news = mock_document(content=title+"\n"+content, is_news=True)
    news.thread = thread
    news.save()
    return thread

def mock_thread_for_annotated_topics(annotation, topic_name, thread_number=0):
    title = annotation[0]
    content = annotation[1]
    thread = mock_thread_with_news(title, content, thread_number)
    topic = mock_topic(topic_name)
    thread.assign_topic(topic)
    return thread
