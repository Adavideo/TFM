from django.test import TestCase
from topics_identifier.topic_clusters import *
from .examples_topics import *
from .mock_topics import mock_topic_with_clusters, mock_threads_and_clusters_with_topic
from .validations import validate_documents_content


class TopicClustersTests(TestCase):

    def test_get_topic_clusters_with_documents(self):
        topic, topic_clusters = mock_topic_with_clusters()
        clusters_with_documents = get_topic_clusters_with_documents(topic)
        for i in range(len(topic_clusters)):
            cluster = clusters_with_documents[i]["cluster"]
            self.assertEqual(cluster, topic_clusters[i])
            documents = cluster.documents()
            expected = topic_clusters[i].documents()
            self.assertNotEqual(len(expected), 0)
            for i in range(len(expected)):
                self.assertEqual(documents[i].content, expected[i].content )

    def test_get_clusters_documents(self):
        topic = mock_threads_and_clusters_with_topic()
        clusters_documents = get_clusters_documents(topic)
        validate_documents_content(self, clusters_documents, example_clusters_documents)

    def test_get_labeled_documents(self):
        topic = mock_threads_and_clusters_with_topic()
        labeled_documents = get_labeled_documents(topic)
        validate_documents_content(self, labeled_documents, example_labeled_documents)

    def test_get_documents_to_label(self):
        topic = mock_threads_and_clusters_with_topic()
        documents_to_label = get_documents_to_label(topic)
        validate_documents_content(self, documents_to_label, example_documents_to_label)
