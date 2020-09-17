from django.test import TestCase
from topics_identifier.TreeGenerator import TreeGenerator
from topics_identifier.ClustersGenerator import ClustersGenerator
from .mock_documents import mock_documents
from .mock_generators import mock_tree_generator, mock_clusters_generator
from .example_trees import tree_name, example_tree
from .examples import test_model_name, test_batch_size
from .examples_documents_selector import example_doc_options, doc_options_with_batches
from .validations_trees import *
from .validations_batches import validate_batch_documents


class TreeGeneratorTests(TestCase):

    def test_create_tree_generator(self):
        tree_generator = mock_tree_generator()
        tree = tree_generator.tree
        self.assertEqual(tree.name, tree_name)
        validate_tree_document_types(self, tree, example_doc_options["types"])
        self.assertEqual(tree_generator.model_name, test_model_name)
        self.assertEqual(tree_generator.tree.name, tree_name)


class GenerateTreeStructureTests(TestCase):

    def test_create_empty_tree(self):
        tree_generator = TreeGenerator("", test_model_name, example_doc_options)
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
        validate_tree_level(self, tree_generator.tree, level,
                            with_documents=False, with_children=False)

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
        validate_tree_level(self, tree_generator.tree, level,
                            with_documents=False, with_children=False)


class AddDocumentsToClustersTests(TestCase):

    def test_get_all_level_documents_level0(self):
        # Initialize
        level = 0
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        # Execute
        documents = tree_generator.get_all_level_documents(level)
        # Validate
        expected_documents = example_tree[level]["documents"]
        self.assertEqual(documents, expected_documents)

    def test_get_all_level_documents_level1(self):
        # Initialize
        level = 1
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        tree_generator.level_iteration(level=0)
        # Execute
        documents = tree_generator.get_all_level_documents(level)
        # Validate
        expected_documents = example_tree[level]["documents"]
        self.assertEqual(documents, expected_documents)

    def test_get_documents_level0(self):
        # Initialize
        level = 0
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        # Execute
        documents = tree_generator.get_documents(level)
        # Validate
        expected_documents = example_tree[level]["documents"]
        self.assertEqual(documents, expected_documents)

    def test_get_documents_level1(self):
        # Initialize
        level = 1
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        tree_generator.level_iteration(level=0)
        # Execute
        documents = tree_generator.get_documents(level)
        # Validate
        expected_documents = example_tree[level]["documents"]
        self.assertEqual(documents, expected_documents)

    def test_get_number_of_documents_level0(self):
        # Initialize
        level = 0
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        tree_generator.level_iteration(level=level)
        # Execute
        num_documents = tree_generator.get_number_of_documents(level)
        # Validate
        expected_num_docs = len(example_tree[level]["documents"])
        self.assertEqual(num_documents, expected_num_docs)

    def test_get_number_of_documents_level1(self):
        # Initialize
        level = 1
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
        tree_generator.level_iteration(level=0)
        tree_generator.level_iteration(level=level)
        # Execute
        num_documents = tree_generator.get_number_of_documents(level)
        # Validate
        expected_num_docs = len(example_tree[level]["documents"])
        self.assertEqual(num_documents, expected_num_docs)

    def test_add_documents_to_clusters_level0(self):
        # Initialize
        level = 0
        mock_documents()
        tree_generator = mock_tree_generator(max_level=1)
        clusters_generator = mock_clusters_generator(level)
        documents = example_tree[level]["documents"]
        # Execute
        tree_generator.add_documents_to_clusters(clusters_generator, documents=documents, level=level)
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
        tree_generator.add_documents_to_clusters(clusters_generator, documents=documents, level=level)
        # Validate
        validate_level_clusters_documents(self, tree_generator.tree, level)


def validate_get_documents_with_batches(test, level, batch_number):
    mock_documents()
    tree_generator = TreeGenerator( "name"+str(level)+str(batch_number),
                                    test_model_name, doc_options_with_batches)
    if level > 0:
        tree_generator.level_iteration(0)
    # Execute
    documents = tree_generator.get_documents(level, batch_number, test_batch_size)
    # Validate
    validate_batch_documents(test, level, batch_number, documents)


class AddDocumentsWithBatchesTest(TestCase):

    def test_get_documents_with_batches(self):
        validate_get_documents_with_batches(self, level=0, batch_number=1)
        validate_get_documents_with_batches(self, level=0, batch_number=2)
        validate_get_documents_with_batches(self, level=1, batch_number=1)
        validate_get_documents_with_batches(self, level=1, batch_number=2)

    def test_add_documents_to_clusters_in_batches(self):
        # Initialize
        level = 0
        mock_documents()
        tree_generator = mock_tree_generator(level, doc_options_with_batches)
        clusters_generator = mock_clusters_generator(level)
        # Execute
        tree_generator.add_documents_to_clusters_in_batches(clusters_generator, level)
        # Validate
        validate_level_clusters_documents(self, tree_generator.tree, level)

    def test_add_documents_with_batches(self):
        # Initialize
        level = 0
        mock_documents()
        tree_generator = mock_tree_generator(level, doc_options_with_batches)
        clusters_generator = mock_clusters_generator(level)
        # Execute
        tree_generator.add_documents(clusters_generator, level)
        # Validate
        validate_level_clusters_documents(self, tree_generator.tree, level)


class MainLoopTests(TestCase):

    def test_level_iteration_level0(self):
        level = 0
        mock_documents()
        tree_generator = mock_tree_generator(max_level=level)
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
        tree_generator = TreeGenerator(tree_name, test_model_name, example_doc_options, max_level=1)
        clusters_level1 = tree_generator.generate_tree()
        clusters_level0 = tree_generator.tree.get_clusters_of_level(level=0)
        self.assertEqual(len(clusters_level0), 4)
        self.assertEqual(str(clusters_level0[0]), "Cluster - tree test_comments10, level 0, num cluster 0")
        self.assertEqual(str(clusters_level0[1]), "Cluster - tree test_comments10, level 0, num cluster 1")
        self.assertEqual(len(clusters_level1), 2)
        self.assertEqual(str(clusters_level1[0]), "Cluster - tree test_comments10, level 1, num cluster 0")
        self.assertEqual(str(clusters_level1[1]), "Cluster - tree test_comments10, level 1, num cluster 1")
