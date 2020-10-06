from django.test import TestCase
from topics_identifier.TreeGenerator import TreeGenerator
from topics_identifier.ClustersGenerator import ClustersGenerator
from .examples import test_batch_size, test_model_name
from .example_trees import tree_name, example_tree
from .mocks import mock_documents
from .mock_generators import mock_tree_generator, mock_clusters_generator
from .validations_trees import *
from .validations_batches import validate_batch_documents


class TreeGeneratorTests(TestCase):

    def test_create_tree_generator_max_level_0(self):
        max_level = 0
        tree_generator = mock_tree_generator(max_level=max_level)
        tree = tree_generator.tree
        # Validate
        self.assertEqual(tree.name, tree_name)
        validate_tree_documents_types(self, tree, documents_types="both")
        self.assertEqual(tree_generator.model_name, test_model_name)
        self.assertEqual(tree_generator.tree.name, tree_name)
        self.assertEqual(tree_generator.tree.max_level, max_level)

    def test_create_tree_generator_max_level_1(self):
        max_level = 1
        tree_generator = mock_tree_generator(max_level=max_level)
        tree = tree_generator.tree
        # Validate
        self.assertEqual(tree.name, tree_name)
        validate_tree_documents_types(self, tree, documents_types="both")
        self.assertEqual(tree_generator.model_name, test_model_name)
        self.assertEqual(tree_generator.tree.name, tree_name)
        self.assertEqual(tree_generator.tree.max_level, max_level)


class GenerateTreeStructureTests(TestCase):

    def test_create_empty_tree(self):
        tree_generator = TreeGenerator("", test_model_name, documents_types="both")
        tree = tree_generator.create_empty_tree(tree_name)
        self.assertEqual(tree.name, tree_name)

    def test_generate_level_clusters_level0(self):
        # Initialize
        mock_documents()
        level = 0
        tree_generator = mock_tree_generator(max_level=level)
        clusters_generator = mock_clusters_generator(level=level)
        # Execute
        tree_generator.generate_level_clusters(clusters_generator, level)
        # Validate
        validate_tree_level(self, tree_generator.tree, level, with_documents=False, with_children=False)

    def test_generate_level_clusters_level1(self):
        # Initialize
        mock_documents()
        level = 1
        tree_generator = mock_tree_generator(max_level=level)
        tree_generator.level_iteration(level=0)
        # Execute
        clusters_generator = ClustersGenerator(tree_generator.model_name, level)
        tree_generator.generate_level_clusters(clusters_generator, level)
        # Validate
        validate_tree_level(self, tree_generator.tree, level, with_documents=False, with_children=False)


class AddDocumentsToClustersTests(TestCase):

    # add_documents_to_clusters

    def test_add_documents_to_clusters_level0(self):
        # Initialize
        level = 0
        mock_documents()
        tree_generator = mock_tree_generator(max_level=1)
        clusters_generator = mock_clusters_generator(level)
        documents = example_tree[level]["documents"]
        # Execute
        tree_generator.add_documents_to_clusters(clusters_generator, documents, level)
        # Validate
        validate_level_clusters_documents(self, tree_generator.tree, level)

    def test_add_documents_to_clusters_level1(self):
        # Initialize
        level = 1
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        clusters_generator = mock_clusters_generator(level)
        documents = example_tree[level]["documents"]
        # Execute
        tree_generator.add_documents_to_clusters(clusters_generator, documents, level)
        # Validate
        validate_level_clusters_documents(self, tree_generator.tree, level)


    # add_documents_level0

    def test_add_documents_level0(self):
        # Initialize
        level = 0
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        # Execute
        tree_generator.add_documents_level0()
        # Validate
        validate_level_clusters_documents(self, tree_generator.tree, level)


    # get_upper_levels_documents

    def test_get_upper_level_documents_level1(self):
        # Initialize
        level = 1
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        tree_generator.level_iteration(level=0)
        # Execute
        documents = tree_generator.get_upper_level_documents(level)
        # Validate
        expected_documents = example_tree[level]["documents"]
        self.assertEqual(documents, expected_documents)


    # add_documents

    def test_add_documents_level0(self):
        # Initialize
        level = 0
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        clusters_generator = mock_clusters_generator(level)
        # Execute
        documents = tree_generator.add_documents(clusters_generator, level)
        # Validate
        validate_level_clusters_documents(self, tree_generator.tree, level)

    def test_add_documents_level1(self):
        # Initialize
        level = 1
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        tree_generator.level_iteration(level=0)
        clusters_generator = mock_clusters_generator(level)
        # Execute
        documents = tree_generator.add_documents(clusters_generator, level)
        # Validate
        validate_level_clusters_documents(self, tree_generator.tree, level)


class MainLoopTests(TestCase):

    def test_level_iteration_level0(self):
        # Initialize
        level = 0
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        # Execute
        tree_generator.level_iteration(level)
        # Validate
        validate_tree(self, tree_generator.tree, max_level=level, documents_types="both")

    def test_level_iteration_level1(self):
        # Initialize
        level = 1
        mock_documents()
        tree_generator = mock_tree_generator()
        tree_generator.level_iteration(level-1)
        # Execute
        tree_generator.level_iteration(level)
        # Validate
        validate_tree(self, tree_generator.tree, max_level=level, documents_types="both")

    def test_generate_tree(self):
        # Initialize
        mock_documents()
        tree_generator = TreeGenerator(tree_name, test_model_name, documents_types="both", max_level=1)
        # Execute
        tree = tree_generator.generate_tree()
        # Validate
        clusters_level0 = tree.get_clusters_of_level(level=0)
        self.assertEqual(len(clusters_level0), len(example_tree[0]["clusters"]))
        self.assertEqual(str(clusters_level0[0]), "Cluster - tree test_comments10, level 0, num cluster 0")
        self.assertEqual(str(clusters_level0[1]), "Cluster - tree test_comments10, level 0, num cluster 1")
        self.assertEqual(str(clusters_level0[2]), "Cluster - tree test_comments10, level 0, num cluster 2")
        clusters_level1 = tree.get_clusters_of_level(level=1)
        self.assertEqual(len(clusters_level1), len(example_tree[1]["clusters"]))
        self.assertEqual(str(clusters_level1[0]), "Cluster - tree test_comments10, level 1, num cluster 0")
