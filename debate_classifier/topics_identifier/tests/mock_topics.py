from timeline.models import Document
from topics_identifier.models import ClusterTopic
from common.testing.mock_topics import mock_topic
from common.testing.mock_threads import mock_threads_with_topic
from .mock_clusters import mock_clusters_list


def mock_topic_with_clusters(topic_name="test", with_documents=True):
    topic = mock_topic(topic_name)
    clusters_list = mock_clusters_list(with_documents=with_documents)
    for cluster in clusters_list:
        ct = ClusterTopic(topic=topic, cluster=cluster)
        ct.save()
    return topic, clusters_list

def mock_threads_and_clusters_with_topic():
    topic, clusters_list = mock_topic_with_clusters()
    threads = mock_threads_with_topic(topic)
    return topic
