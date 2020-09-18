from django.test import TestCase
from topics_identifier.forms_util import *
from .mocks import mock_topic


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
