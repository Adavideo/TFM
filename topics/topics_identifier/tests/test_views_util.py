from django.test import TestCase
from topics_identifier.views_util import *
from topics_identifier.TreeGenerator import TreeGenerator
from .mocks import mock_topic
from .mock_documents import mock_documents
from .mock_web_client import post_request
from .examples import test_model_name


class ViewsUtilTests(TestCase):

    def test_get_documents_options(self):
        options = get_documents_options()
        expected = [('news', 'news'), ('comments', 'comments'), ('both', 'both')]
        self.assertEqual(options, expected)

    def test_get_topics_options_none(self):
        options = get_topics_options()
        expected = [('', '')]
        self.assertEqual(options, expected)

    def test_get_topics_options_one_option(self):
        mock_topic("test")
        options = get_topics_options()
        self.assertEqual(len(options), 1)
        self.assertEqual(str(options[0]), "(1, <Topic: test>)")

    def test_get_tree_levels(self):
        tree_levels = get_tree_levels()
        expected = [(0, '0'), (1, '1')]
        self.assertEqual(tree_levels, expected)

    def test_build_tree_generator(self):
        #Initialize
        level=1
        page = 'generate_tree'
        tree_name = "prueba"
        parameters = { "tree_name": tree_name,"model_name":test_model_name, "document_types":"both"}
        mock_documents()
        request = post_request(page, parameters)
        self.assertEqual(request.method, "POST")
        #Execute
        tree_generator = build_tree_generator(request, level)
        #Validate
        self.assertEqual(str(type(tree_generator)), "<class 'topics_identifier.TreeGenerator.TreeGenerator'>")
        self.assertEqual(tree_generator.tree.name, tree_name)
