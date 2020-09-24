from django.test import TestCase
from models_generator.forms_util import get_documents_options, get_tree_levels


class FormsUtilTests(TestCase):

    def test_get_documents_options(self):
        options = get_documents_options()
        expected = [('news', 'news'), ('comments', 'comments'), ('both', 'both')]
        self.assertEqual(options, expected)

    def test_get_tree_levels(self):
        tree_levels = get_tree_levels()
        expected = [(0, '0'), (1, '1')]
        self.assertEqual(tree_levels, expected)
