from django.test import TestCase
from topics_identifier.topics_clustering import *
from .mocks import mock_threads_with_topic
from .mock_datasets import mock_dataset_from_topics
from .mock_generators import mock_model
from .examples import all_threads_content, test_model_name
from .example_topics import topic, example_terms, example_reference_documents
from .test_datasets_manager import validate_dataset

def mock_clusters_for_topic():
    dataset = mock_dataset_from_topics(topic)
    model = mock_model()
    clusters_information, documents_clusters = generate_clusters_for_topic(model, dataset)
    return clusters_information, documents_clusters


class TopicsTests(TestCase):

    def test_get_dataset_for_topic(self):
        mock_threads_with_topic(topic)
        dataset = get_dataset_for_topic(topic)
        validate_dataset(self, dataset, all_threads_content)

    def test_generate_clusters_for_topic(self):
        clusters_information, documents_clusters = mock_clusters_for_topic()
        self.assertEqual(len(clusters_information), 2)
        self.assertEqual(clusters_information["terms"], example_terms)
        self.assertEqual(clusters_information["reference_documents"], example_reference_documents)

    def test_generate_tree_for_topic(self):
        clusters_information, documents_clusters = mock_clusters_for_topic()
        clusters_list = generate_tree_for_topic(topic.name, clusters_information, documents_clusters)

    def test_generate_tree_for_topic_twice(self):
        clusters_information, documents_clusters = mock_clusters_for_topic()
        generate_tree_for_topic(topic.name, clusters_information, documents_clusters)
        generate_tree_for_topic(topic.name, clusters_information, documents_clusters)

    def test_cluster_for_topic(self):
        mock_dataset_from_topics(topic)
        clusters_list = cluster_for_topic(topic, test_model_name)
        self.assertEqual(len(clusters_list), len(example_terms))
        self.assertEqual(str(clusters_list[0]), "Cluster - tree prueba, level 0, num cluster 0")
