from django.test import TestCase
from topics_identifier.models import Cluster, Tree
from topics_identifier.TreeGenerator import TreeGenerator, short_document_types
from .example_trees import example_tree, tree_name, example_documents_clusters
from .example_stop_words import example_stop_words
from .mock_trees import mock_empty_tree
from .mock_generators import mock_tree_generator
from .mocks import mock_documents
from .validations_clusters import validate_clusters_list
from .validations_trees import validate_tree_level, validate_tree_document_types
from .validations_generators import validate_clusters_terms, validate_clusters_reference_documents


class TreeGeneratorTests(TestCase):

    def test_short_document_types_both(self):
        news, comments = short_document_types(document_types="both")
        self.assertEqual(news, True)
        self.assertEqual(comments, True)

    def test_short_document_types_news(self):
        news, comments = short_document_types(document_types="news")
        self.assertEqual(news, True)
        self.assertEqual(comments, False)

    def test_short_document_types_comments(self):
        news, comments = short_document_types(document_types="comments")
        self.assertEqual(news, False)
        self.assertEqual(comments, True)

    def test_create_tree_generator(self):
        document_types = "both"
        max_level = 1
        generator = TreeGenerator(tree_name="", document_types=document_types, max_level=max_level)
        validate_tree_document_types(self, generator.tree, document_types)

    def test_create_tree_generator_with_tree_name_that_already_exist(self):
        max_level = 1
        tree = Tree(name=tree_name, news=False, comments=True)
        tree.save()
        generator = TreeGenerator(tree_name=tree_name, document_types="news", max_level=max_level)
        self.assertEqual(generator.tree, None)

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
