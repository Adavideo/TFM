from timeline.tests.mocks_threads import mock_thread, mock_threads_list, mock_threads_with_topic
from timeline.models import Topic

def mock_topic(name="test_topic"):
    topic = Topic(name=name)
    topic.save()
    return topic
