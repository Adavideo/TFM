from django.test import TestCase
from topics_identifier.ModelGenerator import ModelGenerator
from .example_trees import example_documents_clusters
from .examples import example_documents
from .mock_generators import mock_cluster_generator
from .validations_generators import validate_clusters_terms, validate_clusters_reference_documents


class ClustersGeneratorTests(TestCase):

    def test_get_clusters_reference_documents(self):
        # Initialize
        generator = mock_cluster_generator()
        # Execute
        reference_documents_list = generator.get_clusters_reference_documents()
        # Validate
        validate_clusters_reference_documents(self, reference_documents_list, level=0)

    def test_get_all_clusters_terms(self):
        # Initialize
        generator = mock_cluster_generator()
        # Execute
        clusters_terms = generator.get_all_clusters_terms()
        # Validate
        validate_clusters_terms(self, clusters_terms, level=0)

    def test_get_clusters_information(self):
        # Initialize
        generator = mock_cluster_generator()
        # Execute
        clusters_information = generator.get_clusters_information()
        # Validate
        validate_clusters_terms(self, clusters_information["terms"], level=0)
        validate_clusters_reference_documents(self, clusters_information["reference_documents"], level=0)

    def test_get_documents_clusters(self):
        # Initialize
        cluster_generator = mock_cluster_generator()
        model_generator = ModelGenerator(example_documents)
        vectorized_documents = model_generator.process_documents()
        # Execute
        documents_clusters = cluster_generator.get_documents_clusters(vectorized_documents)
        # Validate
        self.assertEqual(documents_clusters, example_documents_clusters[0])
