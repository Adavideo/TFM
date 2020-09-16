from django.test import TestCase
from topics_identifier.TreeGenerator import TreeGenerator
from topics_identifier.ClustersGenerator import ClustersGenerator
from .mock_documents import mock_documents
from .mock_trees import mock_tree
from .mock_generators import mock_tree_generator, mock_clusters_generator
from .example_trees import tree_name, example_tree
from .examples import test_model_name
from .examples_documents_selector import example_doc_options
from .example_documents import example_documents
from .validations import validate_dataset
from .validations_trees import validate_tree_document_types, validate_tree
from .validations_clusters import validate_clusters_list, validate_cluster
from .validations_documents import validate_documents


class TreeGeneratorTests(TestCase):

    def test_create_tree_generator(self):
        generator = mock_tree_generator()
        tree = generator.tree
        self.assertEqual(tree.name, tree_name)
        validate_tree_document_types(self, tree, example_doc_options["types"])
        self.assertEqual(generator.model_name, test_model_name)
        self.assertEqual(generator.tree.name, tree_name)

    def test_create_empty_tree(self):
        generator = TreeGenerator("", test_model_name, example_doc_options)
        tree = generator.create_empty_tree(tree_name)
        self.assertEqual(tree.name, tree_name)

    def test_get_documents_level0(self):
        level = 0
        generator = TreeGenerator("", test_model_name, example_doc_options)
        mock_documents()
        documents = generator.get_documents(level)
        self.assertEqual(documents, example_documents)

    def test_get_documents_level1(self):
        level = 1
        generator = TreeGenerator("", test_model_name, example_doc_options)
        mock_documents()
        generator.level_iteration(level=0)
        documents = generator.get_documents(level)
        documents_level1 = example_tree[1]["documents"]
        self.assertEqual(documents, documents_level1)

    def test_generate_level_clusters_level0(self):
        # Initialize
        mock_documents()
        level = 0
        tree_generator = mock_tree_generator(max_level=level)
        clusters_generator = mock_clusters_generator(level=level)
        # Execute
        tree_generator.generate_level_clusters(clusters_generator, level)
        # Validate
        clusters_list = tree_generator.tree.get_clusters_of_level(level)
        example_clusters = example_tree[level]["clusters"]
        validate_clusters_list(self, clusters_list, example_clusters, with_documents=False)

    def test_generate_level_clusters_level1(self):
        # Initialize
        mock_documents()
        level = 1
        tree_generator = mock_tree_generator(max_level=level)
        tree_generator.level_iteration(level=0)
        # Execute
        clusters_generator = ClustersGenerator(tree_generator.models_manager, level)
        tree_generator.generate_level_clusters(clusters_generator, level)
        # Validate
        clusters_list = tree_generator.tree.get_clusters_of_level(level)
        expected_clusters = example_tree[level]["clusters"]
        validate_clusters_list(self, clusters_list, expected_clusters, with_documents=True, with_children=False)

    def test_add_documents_to_clusters_level0(self):
        # Initialize
        mock_documents()
        level = 0
        tree_generator = mock_tree_generator(max_level=1)
        clusters_generator = mock_clusters_generator()
        documents = example_tree[level]["documents"]
        # Execute
        tree_generator.add_documents_to_clusters(clusters_generator, documents=documents, level=level)
        # Validate
        clusters_list = tree_generator.tree.get_clusters_of_level(level=level)
        example_clusters = example_tree[level]["clusters"]
        for i in range(len(clusters_list)):
            cluster_documents = clusters_list[i].documents()
            validate_documents(self, cluster_documents, example_clusters[i]["documents"])

    def test_add_documents_to_clusters_level1(self):
        # Initialize
        mock_documents()
        level = 1
        tree_generator = mock_tree_generator(max_level=level)
        clusters_generator = mock_clusters_generator(level)
        documents = example_tree[level]["documents"]
        # Execute
        tree_generator.add_documents_to_clusters(clusters_generator, documents=documents, level=level)
        # Validate
        clusters_list = tree_generator.tree.get_clusters_of_level(level=level)
        example_clusters = example_tree[level]["clusters"]
        for i in range(len(clusters_list)):
            cluster_documents = clusters_list[i].documents()
            validate_documents(self, cluster_documents, example_clusters[i]["documents"])

    def test_level_iteration_level0(self):
        level = 0
        mock_documents()
        tree_generator = mock_tree_generator()
        tree_generator.level_iteration(level)
        validate_tree(self, tree_generator.tree, max_level=level, document_types="both")

    def test_level_iteration_level1(self):
        level = 1
        mock_documents()
        tree_generator = mock_tree_generator()
        tree_generator.level_iteration(level-1)
        tree_generator.level_iteration(level)
        validate_tree(self, tree_generator.tree, max_level=level, document_types="both")

    def test_generate_tree(self):
        mock_documents()
        generator = TreeGenerator(tree_name, test_model_name, example_doc_options, max_level=1)
        clusters_level1 = generator.generate_tree()
        clusters_level0 = generator.tree.get_clusters_of_level(level=0)
        self.assertEqual(len(clusters_level0), 4)
        self.assertEqual(str(clusters_level0[0]), "Cluster - tree test_comments10, level 0, num cluster 0")
        self.assertEqual(str(clusters_level0[1]), "Cluster - tree test_comments10, level 0, num cluster 1")
        self.assertEqual(len(clusters_level1), 2)
        self.assertEqual(str(clusters_level1[0]), "Cluster - tree test_comments10, level 1, num cluster 0")
        self.assertEqual(str(clusters_level1[1]), "Cluster - tree test_comments10, level 1, num cluster 1")
