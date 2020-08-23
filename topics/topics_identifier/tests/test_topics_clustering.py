from django.test import TestCase
from topics_identifier.topics_clustering import *
from .mocks import mock_threads_with_topic
from .mock_datasets import mock_dataset_from_topics
from .mock_generators import mock_model, mock_vectorizer, mock_models_manager
from .examples import all_threads_content, example_terms
from .example_topics import topic, topic_model_name, example_reference_documents, example_topics_cluster_terms
from .test_datasets_manager import validate_dataset
from .validations_models import validate_model_stored, validate_vectorizer_stored

from topics_identifier.ModelsManager import ModelsManager
from topics_identifier.ModelGenerator import ModelGenerator


def mock_clusters_for_topic():
    level = 0
    models_manager = mock_models_manager(name=topic_model_name)
    dataset = mock_dataset_from_topics(topic)
    model = models_manager.load_model(level)
    vectorizer = models_manager.load_vectorizer(level)
    clusters_information = generate_clusters_for_topic(model, dataset, vectorizer)
    return clusters_information


class TopicsTests(TestCase):

    def test_create_model_for_topic(self):
        # Initialize
        level = 0
        topic_name = "delete_me_topic"
        topic = Topic(name=topic_name)
        mock_threads_with_topic(topic)
        # Execute
        create_and_store_model_for_topic(topic)
        # Validate
        validate_model_stored(self, topic_name, level)
        validate_vectorizer_stored(self, topic_name, level)

    def test_get_dataset_for_topic(self):
        mock_threads_with_topic(topic)
        dataset = get_dataset_for_topic(topic)
        validate_dataset(self, dataset, all_threads_content)

    def test_generate_clusters_for_topic(self):
        clusters_information = mock_clusters_for_topic()
        self.assertEqual(len(clusters_information), 2)
        self.assertEqual(clusters_information["terms"], example_topics_cluster_terms)
        self.assertEqual(clusters_information["reference_documents"], example_reference_documents)

    def test_generate_tree_for_topic(self):
        clusters_information = mock_clusters_for_topic()
        clusters_list = generate_tree_for_topic(topic.name, clusters_information)

    def test_generate_tree_for_topic_twice(self):
        clusters_information = mock_clusters_for_topic()
        generate_tree_for_topic(topic.name, clusters_information)
        generate_tree_for_topic(topic.name, clusters_information)

    def test_cluster_for_topic(self):
        mock_dataset_from_topics(topic)
        clusters_list = cluster_for_topic(topic, topic_model_name)
        self.assertEqual(len(clusters_list), len(example_reference_documents))
        self.assertEqual(str(clusters_list[0]), "Cluster - tree prueba, level 0, num cluster 0")
