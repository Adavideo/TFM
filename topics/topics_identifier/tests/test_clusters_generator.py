from django.test import TestCase
from .example_trees import example_tree, example_predicted_clusters, example_reference_documents
from .examples import example_documents, example_terms
from .mock_generators import mock_clusters_generator
from .mocks import mock_documents
from .validations_generators import validate_clusters_reference_documents
from .validations_models import model_type, vectoricer_type
from .validations_clusters import validate_clusters_documents, validate_clusters_terms, validate_clusters_without_tree


class ClustersGeneratorTests(TestCase):

    def test_create_clusters_generator(self):
        level = 0
        clusters_generator = mock_clusters_generator(level)
        self.assertEqual(str(type(clusters_generator.model)), model_type)
        self.assertEqual(str(type(clusters_generator.vectorizer)), vectoricer_type)
        self.assertEqual(clusters_generator.reference_documents, example_reference_documents[level])
        self.assertEqual(clusters_generator.terms, example_terms)
        num_clusters = len(example_tree[level]["clusters"])
        self.assertEqual(clusters_generator.number_of_clusters, num_clusters)

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
        generator = mock_clusters_generator(level)
        clusters_list = generator.get_clusters()
        validate_clusters_without_tree(self, clusters_list, level)

    def test_generate_reference_documents(self):
        level = 0
        mock_documents()
        clusters_generator = mock_clusters_generator(level)
        documents = example_tree[level]["documents"]
        reference_documents_list = clusters_generator.get_reference_documents(documents)
        validate_clusters_reference_documents(self, reference_documents_list, level )

    def test_get_documents_grouped_by_cluster(self):
        level = 0
        predicted_clusters = example_predicted_clusters[level]
        clusters_generator = mock_clusters_generator()
        clusters_documents = clusters_generator.get_documents_grouped_by_cluster(example_documents, predicted_clusters)
        validate_clusters_documents(self, clusters_documents, level)

    def test_predict_clusters_documents(self):
        clusters_generator = mock_clusters_generator()
        clusters_documents = clusters_generator.predict_clusters_documents(documents=example_documents)
        validate_clusters_documents(self, clusters_documents, level=0)
