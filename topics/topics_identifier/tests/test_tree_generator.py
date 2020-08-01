from django.test import TestCase
from topics_identifier.models import Cluster
from .examples import example_tree, example_stop_words, example_documents_clusters
from .mocks import mock_documents, mock_tree_generator
from .validations import validate_clusters_terms, validate_tree_level, validate_clusters_reference_documents, validate_clusters_list


class TreeGeneratorTests(TestCase):

    def test_get_stop_words(self):
        tree_generator = mock_tree_generator(max_level=0)
        stop_words = tree_generator.get_stop_words()
        self.assertEqual(stop_words, example_stop_words)

    def test_cluster_level_0(self):
        level = 0
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        clusters_information, documents_clusters = tree_generator.cluster_level(level)
        # Verify
        validate_clusters_terms(self, clusters_information["terms"], level)
        validate_clusters_reference_documents(self, clusters_information["reference_documents"], level)
        self.assertEqual(documents_clusters, example_documents_clusters[level])

    def test_cluster_level1(self):
        # Initialize
        level = 1
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        clusters_information0, documents_clusters0 = tree_generator.cluster_level(level-1)
        tree_generator.store_information(level-1, clusters_information0, documents_clusters0)
        # Execute
        clusters_information1, documents_clusters1 = tree_generator.cluster_level(level)
        # Validate
        validate_clusters_terms(self, clusters_information1["terms"], level)
        validate_clusters_reference_documents(self, clusters_information1["reference_documents"], level)
        self.assertEqual(documents_clusters1, example_documents_clusters[level])

    def test_store_information(self):
        # Initialize
        level = 0
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        clusters_information, documents_clusters = tree_generator.cluster_level(level)
        # Execute
        tree_generator.store_information(level, clusters_information, documents_clusters)
        # Validate
        clusters = Cluster.objects.filter(tree=tree_generator.tree, level=level)
        example_clusters = example_tree[level]["clusters"]
        validate_clusters_list(self, clusters, example_clusters, with_documents=True)

    def test_generate_tree_level0(self):
        level = 0
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        tree = tree_generator.generate_tree()
        validate_tree_level(self, tree, level)

    def test_generate_tree_level1(self):
        level = 1
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        tree = tree_generator.generate_tree()
        validate_tree_level(self, tree, level-1)
        validate_tree_level(self, tree, level)
