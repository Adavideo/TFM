from django.test import TestCase
from topics_identifier.TreeGenerator import TreeGenerator
from .mocks import mock_documents
from .mock_trees import mock_tree
from .mock_generators import mock_tree_generator, mock_cluster_generator
from .example_trees import tree_name, example_tree
from .examples import test_model_name, example_doc_options, example_documents
from .validations import validate_dataset
from .validations_trees import validate_tree_document_types
from .validations_clusters import validate_clusters_list


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

    def test_get_dataset_level0(self):
        level = 0
        generator = TreeGenerator("", test_model_name, example_doc_options)
        mock_documents()
        dataset = generator.get_dataset(level)
        validate_dataset(self, dataset, example_documents)

    def test_get_dataset_level1(self):
        level = 1
        generator = TreeGenerator("", test_model_name, example_doc_options)
        mock_documents()
        generator.level_iteration(level=0)
        dataset = generator.get_dataset(level)
        documents_level1 = example_tree[1]["documents"]
        validate_dataset(self, dataset, documents_level1)

    def test_generate_level_clusters(self):
        mock_documents()
        level = 0
        tree_generator = mock_tree_generator(max_level=0)
        clusters_generator = mock_cluster_generator()
        tree_generator.generate_level_clusters(clusters_generator, level)
        clusters_level0 = tree_generator.tree.get_clusters_of_level(level)
        validate_clusters_list(self, clusters_level0, example_tree[level]["clusters"], with_documents=False)

    def test_get_loading_files_errors_both(self):
        tree_generator = mock_tree_generator(max_level=0)
        error = tree_generator.get_loading_files_errors(model=None, vectorizer=None, level=0)
        self.assertEqual(error, "model and vectorizer not loaded for level 0")

    def test_get_loading_files_errors_model(self):
        tree_generator = mock_tree_generator(max_level=0)
        error = tree_generator.get_loading_files_errors(model=None, vectorizer=True, level=0)
        self.assertEqual(error, "model not loaded for level 0")

    def test_get_loading_files_errors_vectorizer(self):
        tree_generator = mock_tree_generator(max_level=0)
        error = tree_generator.get_loading_files_errors(model=True, vectorizer=None, level=0)
        self.assertEqual(error, "vectorizer not loaded for level 0")

    def test_get_loading_files_errors_none(self):
        tree_generator = mock_tree_generator(max_level=0)
        error = tree_generator.get_loading_files_errors(model=True, vectorizer=True, level=0)
        self.assertEqual(error, "")

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
