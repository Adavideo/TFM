from sklearn.datasets.base import Bunch
from .examples import comments_content
from .mocks import mock_thread, mock_threads_with_topic
from topics_identifier.topics_clustering import get_dataset_for_topic


def mock_dataset():
    dataset = Bunch()
    dataset.data = comments_content
    return dataset

def mock_dataset_from_topics(topic):
    threads = mock_threads_with_topic(topic)
    dataset = get_dataset_for_topic(topic)
    return dataset
