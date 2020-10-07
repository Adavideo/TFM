from django.test import TestCase
from common.models_loader import load_object
from topics_identifier.ClustersGenerator import ClustersGenerator
from .examples import test_model_name
from .example_trees import example_tree
from .examples_clustering import example1, example2
from .mocks import mock_documents
from .mock_generators import mock_clusters_generator
from .validations_clusters_generator import *
from .validations_clusters import *


class ClustersGeneratorTests(TestCase):

    def test_create_clusters_generator(self):
        level = 0
        clusters_generator = ClustersGenerator(test_model_name, level)
        validate_clusters_generator(self, clusters_generator, test_model_name, example_tree[level])

    def test_load_model_and_vectorizer_level0(self):
        level=0
        clusters_generator = mock_clusters_generator(level)
        clusters_generator.load_model_and_vectorizer()
        validate_clusters_generator(self, clusters_generator, test_model_name, example_tree[level])

    def test_load_model_and_vectorizer_level1(self):
        level=1
        clusters_generator = mock_clusters_generator(level)
        clusters_generator.load_model_and_vectorizer()
        validate_clusters_generator(self, clusters_generator, test_model_name, example_tree[level])

    def test_load_clusters_information_level0(self):
        level=0
        clusters_generator = mock_clusters_generator(level)
        error = clusters_generator.load_clusters_information()
        self.assertEqual(error, None)
        validate_clusters_information_in_clusters_generator(self, clusters_generator, example_tree[level])

    def test_load_clusters_information_level1(self):
        level=1
        clusters_generator = mock_clusters_generator(level)
        error = clusters_generator.load_clusters_information()
        self.assertEqual(error, None)
        validate_clusters_information_in_clusters_generator(self, clusters_generator, example_tree[level])

    def test_calculate_number_of_clusters(self):
        clusters_generator = mock_clusters_generator()
        number = clusters_generator.calculate_number_of_clusters()
        num_clusters_level0 = len(example_tree[0]["clusters"])
        self.assertEqual(number, num_clusters_level0)

    def test_get_all_clusters_terms(self):
        clusters_generator = mock_clusters_generator()
        clusters_terms = clusters_generator.get_all_clusters_terms()
        validate_clusters_terms(self, clusters_terms, level=0)

    def test_get_clusters(self):
        level = 0
        mock_documents()
        clusters_generator = mock_clusters_generator(level)
        clusters_list = clusters_generator.get_clusters()
        expected_clusters = example_tree[0]["clusters"]
        validate_clusters_list(self, clusters_list, expected_clusters, with_documents=False)

    def test_get_reference_documents(self):
        # Initialize
        level = 0
        mock_documents()
        clusters_generator = mock_clusters_generator(level)
        original_documents_content = example_tree[level]["documents"]
        # Execute
        reference_documents_content = clusters_generator.get_reference_documents(original_documents_content)
        # Validate
        expected_documents = example_tree[level]["reference_documents"]
        self.assertEqual(reference_documents_content, expected_documents)

    def test_get_documents_grouped_by_cluster_with_same_documents(self):
        clusters_generator = mock_clusters_generator()
        documents = mock_documents(example1["documents"])
        clusters_documents = clusters_generator.get_documents_grouped_by_cluster(documents, example1["predicted_clusters"])
        validate_clusters_documents(self, clusters_documents, example1)

    def test_get_documents_grouped_by_cluster_with_diferent_documents(self):
        clusters_generator = mock_clusters_generator()
        documents = mock_documents(example2["documents"])
        clusters_documents = clusters_generator.get_documents_grouped_by_cluster(documents, example2["predicted_clusters"])
        validate_clusters_documents(self, clusters_documents, example2)

    def test_predict_clusters_documents_with_same_documents(self):
        clusters_generator = mock_clusters_generator()
        documents = mock_documents(example1["documents"])
        clusters_documents = clusters_generator.predict_clusters_documents(documents)
        validate_clusters_documents(self, clusters_documents, example1)

    def test_predict_clusters_documents_with_diferent_documents(self):
        clusters_generator = mock_clusters_generator()
        documents = mock_documents(example2["documents"])
        clusters_documents = clusters_generator.predict_clusters_documents(documents)
        validate_clusters_documents(self, clusters_documents, example2)
