from django.test import TestCase
from .example_trees import example_tree
from .examples import test_model_name
from .examples_clustering import example1, example2
from .mock_generators import mock_clusters_generator, mock_models_manager
from .mock_documents import mock_documents
from .validations_clusters_generator import *
from .validations_clusters import validate_clusters_terms, validate_clusters_list
from topics_identifier.ClustersGenerator import ClustersGenerator


class ClustersGeneratorTests(TestCase):

    def test_create_clusters_generator_loading_model_and_vectorizer_from_files(self):
        level = 0
        models_manager = mock_models_manager(test_model_name)
        clusters_generator = ClustersGenerator(models_manager, level)
        validate_clusters_generator(self, clusters_generator, test_model_name, example_tree[level])

    def test_create_clusters_generator_with_model_and_vectorizer_as_parameters(self):
        level = 0
        models_manager = mock_models_manager(test_model_name)
        model = models_manager.load_object("model", level)
        vectorizer = models_manager.load_object("vectorizer", level)
        clusters_generator = ClustersGenerator(models_manager, level, model, vectorizer)
        validate_clusters_generator(self, clusters_generator, test_model_name, example_tree[level])

    def test_load_model_and_vectorizer_level0(self):
        level=0
        clusters_generator = mock_clusters_generator(level)
        clusters_generator.model = None
        clusters_generator.vectorizer = None
        clusters_generator.load_model_and_vectorizer(model=None, vectorizer=None)
        validate_clusters_generator(self, clusters_generator, test_model_name, example_tree[level])

    def test_load_model_and_vectorizer_level1(self):
        level=1
        clusters_generator = mock_clusters_generator(level)
        clusters_generator.model = None
        clusters_generator.vectorizer = None
        clusters_generator.load_model_and_vectorizer(model=None, vectorizer=None)
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

    def test_generate_reference_documents(self):
        # Initialize
        level = 0
        mock_documents()
        clusters_generator = mock_clusters_generator(level)
        documents = example_tree[level]["documents"]
        # Execute
        reference_documents = clusters_generator.get_reference_documents(documents)
        # Validate
        expected_documents = example_tree[level]["reference_documents"]
        self.assertEqual(reference_documents, expected_documents)

    def test_get_documents_grouped_by_cluster_with_same_documents(self):
        clusters_generator = mock_clusters_generator()
        clusters_documents = clusters_generator.get_documents_grouped_by_cluster(example1["documents"], example1["predicted_clusters"])
        validate_clusters_documents(self, clusters_documents, example1)

    def test_get_documents_grouped_by_cluster_with_diferent_documents(self):
        clusters_generator = mock_clusters_generator()
        clusters_documents = clusters_generator.get_documents_grouped_by_cluster(example2["documents"], example2["predicted_clusters"])
        validate_clusters_documents(self, clusters_documents, example2)

    def test_predict_clusters_documents_with_same_documents(self):
        clusters_generator = mock_clusters_generator()
        clusters_documents = clusters_generator.predict_clusters_documents(documents=example1["documents"])
        validate_clusters_documents(self, clusters_documents, example1)

    def test_predict_clusters_documents_with_diferent_documents(self):
        clusters_generator = mock_clusters_generator()
        clusters_documents = clusters_generator.predict_clusters_documents(documents=example2["documents"])
        validate_clusters_documents(self, clusters_documents, example2)
