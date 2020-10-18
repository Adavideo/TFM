from timeline.models import Topic
from .mocks import mock_thread_with_news


def mock_thread_for_annotated_topic(annotation, topic_name, thread_number=0):
    title = annotation[0]
    content = annotation[1]
    thread = mock_thread_with_news(title, content, thread_number)
    topic, _ = Topic.objects.get_or_create(name=topic_name)
    thread.assign_topic(topic)
    return thread
