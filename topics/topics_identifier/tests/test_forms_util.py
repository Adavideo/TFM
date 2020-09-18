from django.test import TestCase
from topics_identifier.forms_util import *
from .mocks import mock_topic
from .examples import test_model_name, filenames_test_list


class FormsUtilTests(TestCase):

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

    def test_get_model_name_from_filename(self):
        models_names = []
        for filename in filenames_test_list:
            name = get_model_name_from_filename(filename)
            if name:
                models_names.append(name)

        self.assertEqual(len(models_names), 2)
        self.assertEqual(models_names[0], "test")
        self.assertEqual(models_names[1], "test")

    def test_get_models_names(self):
        models_names = get_models_names()
        self.assertNotEqual(len(models_names), 0)
        count = 0
        for name in models_names:
            if name == test_model_name: count += 1
        self.assertEqual(count, 1)

    def test_get_models_options(self):
        options = get_models_options()
        self.assertNotEqual(len(options), 0)
        self.assertEqual( ('test','test') in options, True )
