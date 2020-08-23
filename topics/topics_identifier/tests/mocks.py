from timeline.tests.mock_documents import mock_document, mock_documents, mock_news, mock_comments
from timeline.tests.mocks_threads import mock_thread, mock_threads_list, mock_threads_with_topic

def mock_news_and_comments():
    mock_news(number=0)
    mock_news(number=1)
    mock_comments()
