from django.test import TestCase
from topics_identifier.errors import loading_files_errors
from .mock_generators import mock_tree_generator

class LoadingFilesErrors(TestCase):

    def test_get_loading_files_errors_both(self):
        tree_generator = mock_tree_generator(max_level=0)
        error = loading_files_errors(model=None, vectorizer=None, level=0)
        self.assertEqual(error, "model and vectorizer not loaded for level 0")

    def test_get_loading_files_errors_model(self):
        tree_generator = mock_tree_generator(max_level=0)
        error = loading_files_errors(model=None, vectorizer=True, level=0)
        self.assertEqual(error, "model not loaded for level 0")

    def test_get_loading_files_errors_vectorizer(self):
        tree_generator = mock_tree_generator(max_level=0)
        error = loading_files_errors(model=True, vectorizer=None, level=0)
        self.assertEqual(error, "vectorizer not loaded for level 0")

    def test_get_loading_files_errors_none(self):
        tree_generator = mock_tree_generator(max_level=0)
        error = loading_files_errors(model=True, vectorizer=True, level=0)
        self.assertEqual(error, "")
