from django.test import TestCase
from common.forms import get_topics_options
from topics_identifier.forms_util import *
from .examples import test_model_name, filenames_test_list
from .mocks import mock_topic


class FormsUtilTests(TestCase):

    def test_get_topics_options_none(self):
        options = get_topics_options()
        expected = [('', '')]
        self.assertEqual(options, expected)

    def test_get_topics_options_one_option(self):
        mock_topic("test")
        options = get_topics_options()
        self.assertEqual(len(options), 1)
        self.assertEqual(str(options[0]), "(1, 'test')")

    def test_get_model_name_from_filename(self):
        models_names = []
        for filename in filenames_test_list:
            name = get_model_name_from_filename(filename)
            if name:
                models_names.append(name)
        # Validate
        self.assertEqual(len(models_names), 2)
        self.assertEqual(models_names[0], "news")
        self.assertEqual(models_names[1], "news")

    def test_get_models_names(self):
        models_names = get_models_names()
        self.assertIs(test_model_name in models_names, False)
        if len(models_names)==0:
            self.assertEqual(models_names, [])
        else:
            self.assertEqual(type(models_names[0]), type(""))

    def test_get_models_options(self):
        models_names = get_models_names()
        options = get_models_options()
        if len(models_names)==0:
            self.assertEqual(options, [('','')])
