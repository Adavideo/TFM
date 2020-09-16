from timeline.tests.mock_documents import mock_document, mock_documents, mock_news, mock_comments
from .mocks import mock_threads_with_topic
from topics_identifier.topics_clustering import get_documents_for_topic

def mock_news_and_comments():
    mock_news(number=0)
    mock_news(number=1)
    mock_comments()

def mock_documents_for_topic(topic):
    threads = mock_threads_with_topic(topic)
    documents = get_documents_for_topic(topic)
    return documents
