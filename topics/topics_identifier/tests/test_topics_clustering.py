from django.test import TestCase
from topics_identifier.topics_clustering import create_and_store_model_for_topic, get_dataset_for_topic, get_clusters_generator, generate_tree_for_topic, cluster_for_topic
from topics_identifier.models import Topic
from .mocks import mock_threads_with_topic
from .mock_datasets import mock_dataset_from_topics
from .examples import all_threads_content
from .example_topics import topic, topic_model_name, example_reference_documents
from .test_datasets_manager import validate_dataset
from .validations_models import validate_model_stored, validate_vectorizer_stored


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

    def test_generate_tree_for_topic(self):
        mock_dataset_from_topics(topic)
        clusters_generator = get_clusters_generator(topic, topic_model_name)
        tree_generator = generate_tree_for_topic(topic.name, topic_model_name, clusters_generator)

    def test_cluster_for_topic(self):
        mock_dataset_from_topics(topic)
        clusters_list = cluster_for_topic(topic, topic_model_name)
        self.assertEqual(len(clusters_list), len(example_reference_documents))
        self.assertEqual(str(clusters_list[0]), "Cluster - tree prueba, level 0, num cluster 0")