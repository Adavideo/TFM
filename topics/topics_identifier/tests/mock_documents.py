from .mocks import mock_threads_with_topic
from topics_identifier.topics_clustering import get_documents_for_topic


def mock_documents_for_topic(topic):
    threads = mock_threads_with_topic(topic)
    documents = get_documents_for_topic(topic)
    return documents
