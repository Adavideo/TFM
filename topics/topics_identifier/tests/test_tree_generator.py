from django.test import TestCase
from topics_identifier.TreeGenerator import TreeGenerator
from .mocks import mock_documents
from .example_trees import tree_name
from .examples import test_model_name, example_doc_options
from .validations_trees import validate_tree_document_types


class TreeGeneratorTests(TestCase):

    def test_create_tree_generator(self):
        generator = TreeGenerator(tree_name, test_model_name, example_doc_options)
        tree = generator.tree
        self.assertEqual(tree.name, tree_name)
        validate_tree_document_types(self, tree, example_doc_options["types"])
        self.assertEqual(generator.model_name, test_model_name)

    def test_create_empty_tree(self):
        generator = TreeGenerator("", test_model_name, example_doc_options)
        tree = generator.create_empty_tree(tree_name, example_doc_options["types"])
        self.assertEqual(tree.name, tree_name)

    def test_generate_tree(self):
        mock_documents()
        generator = TreeGenerator(tree_name, test_model_name, example_doc_options)
        clusters = generator.generate_tree()
        self.assertEqual(len(clusters), 2)
        self.assertEqual(str(clusters[0]), "Cluster - tree test_comments10, level 1, num cluster 0")
        self.assertEqual(str(clusters[1]), "Cluster - tree test_comments10, level 1, num cluster 1")
