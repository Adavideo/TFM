from testing_commons.mock_documents import *
from testing_commons.mock_web_client import *
from testing_commons.mock_threads import mock_thread, mock_threads_list
from timeline.models import Topic


def mock_topic(name="test_topic"):
    topic = Topic(name=name)
    topic.save()
    return topic
