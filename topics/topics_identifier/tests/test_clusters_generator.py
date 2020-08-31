from django.test import TestCase
from .example_trees import example_tree, example_predicted_clusters
from .examples import example_documents, example_terms
from .mock_generators import mock_cluster_generator
from .validations_generators import validate_clusters_terms, validate_clusters_reference_documents
from .validations_models import model_type, vectoricer_type
from .validations_clusters import validate_clusters_documents


class ClustersGeneratorTests(TestCase):

    def test_create_cluster_generator(self):
        cluster_generator = mock_cluster_generator()
        self.assertEqual(cluster_generator.original_documents, example_documents)
        self.assertEqual(str(type(cluster_generator.model)), model_type)
        self.assertEqual(str(type(cluster_generator.vectorizer)), vectoricer_type)
        self.assertEqual(cluster_generator.terms, example_terms)
        num_clusters_level0 = len(example_tree[0]["clusters"])
        self.assertEqual(cluster_generator.number_of_clusters, num_clusters_level0)

    def test_calculate_number_of_clusters(self):
        cluster_generator = mock_cluster_generator()
        number = cluster_generator.calculate_number_of_clusters()
        num_clusters_level0 = len(example_tree[0]["clusters"])
        self.assertEqual(number, num_clusters_level0)

    def test_get_all_clusters_terms(self):
        cluster_generator = mock_cluster_generator()
        clusters_terms = cluster_generator.get_all_clusters_terms()
        validate_clusters_terms(self, clusters_terms, level=0)

    def test_get_clusters_reference_documents(self):
        cluster_generator = mock_cluster_generator()
        reference_documents_list = cluster_generator.get_clusters_reference_documents()
        validate_clusters_reference_documents(self, reference_documents_list, level=0)

    def test_get_clusters_information(self):
        level = 0
        generator = mock_cluster_generator()
        clusters_information = generator.get_clusters_information()
        validate_clusters_terms(self, clusters_information["terms"], level)
        validate_clusters_reference_documents(self, clusters_information["reference_documents"], level)

    def test_get_documents_grouped_by_cluster(self):
        level = 0
        predicted_clusters = example_predicted_clusters[level]
        cluster_generator = mock_cluster_generator()
        clusters_documents = cluster_generator.get_documents_grouped_by_cluster(example_documents, predicted_clusters)
        validate_clusters_documents(self, clusters_documents, level)

    def test_predict_clusters_documents(self):
        cluster_generator = mock_cluster_generator()
        clusters_documents = cluster_generator.predict_clusters_documents(documents=example_documents)
        validate_clusters_documents(self, clusters_documents, level=0)
