from django.test import TestCase
from .example_trees import example_tree, example_documents_clusters
from .mock_generators import mock_cluster_generator
from .validations_generators import validate_clusters_terms, validate_clusters_reference_documents


class ClustersGeneratorTests(TestCase):

    def test_process_data(self):
        # Initialize
        generator = mock_cluster_generator()
        example_terms = example_tree[0]["terms"]
        # Execute
        generator.process_data()
        # Validate
        self.assertEqual(generator.terms, example_terms)
        self.assertEqual(str(type(generator.vectorized_documents)), "<class 'scipy.sparse.csr.csr_matrix'>")

    def test_get_clusters_reference_documents(self):
        # Initialize
        generator = mock_cluster_generator()
        generator.process_data()
        generator.train_model()
        # Execute
        reference_documents_list = generator.get_clusters_reference_documents()
        # Validate
        validate_clusters_reference_documents(self, reference_documents_list, level=0)

    def test_get_all_clusters_terms(self):
        # Initialize
        generator = mock_cluster_generator()
        generator.process_data()
        generator.train_model()
        # Execute
        clusters_terms = generator.get_all_clusters_terms()
        # Validate
        validate_clusters_terms(self, clusters_terms, level=0)

    def test_get_clusters_information(self):
        # Initialize
        generator = mock_cluster_generator()
        generator.process_data()
        generator.train_model()
        # Execute
        clusters_information = generator.get_clusters_information()
        # Validate
        validate_clusters_terms(self, clusters_information["terms"], level=0)
        validate_clusters_reference_documents(self, clusters_information["reference_documents"], level=0)

    def test_cluster_data(self):
        # Initialize
        generator = mock_cluster_generator()
        # Execute
        clusters_information = generator.cluster_data()
        # Validate
        validate_clusters_terms(self, clusters_information["terms"], level=0)
        validate_clusters_reference_documents(self, clusters_information["reference_documents"], level=0)

    def test_get_documents_clusters(self):
        # Initialize
        generator = mock_cluster_generator()
        clusters_information = generator.cluster_data()
        # Execute
        documents_clusters = generator.get_documents_clusters()
        # Validate
        self.assertEqual(documents_clusters, example_documents_clusters[0])
