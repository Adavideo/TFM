from sklearn.datasets.base import Bunch
from .examples import comments_content
from .mocks import mock_thread
from topics_identifier.topics_manager import get_dataset_for_topic


def mock_dataset():
    dataset = Bunch()
    dataset.data = comments_content
    return dataset

def mock_dataset_from_topics(topic):
    mock_thread(thread_number=0, with_documents=True, news_number=0)
    mock_thread(thread_number=1, with_documents=True, news_number=1)
    dataset = get_dataset_for_topic(topic)
    return dataset
