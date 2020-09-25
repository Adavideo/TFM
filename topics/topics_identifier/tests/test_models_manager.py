from django.test import TestCase
from sklearn.cluster import AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer
from .examples import example_reference_documents
from .mock_generators import mock_models_manager


class ModelsManagerTests(TestCase):

    def test_get_filename_model(self):
        manager = mock_models_manager(name="test")
        filename = manager.get_filename("model", level=0)
        self.assertEqual(filename, "models/sklearn/test_model_level0.joblib")

    def test_get_filename_vectorizer(self):
        manager = mock_models_manager(name="test")
        filename = manager.get_filename("vectorizer", level=0)
        self.assertEqual(filename, "models/sklearn/test_vectorizer_level0.joblib")

    def test_load_model(self):
        manager = mock_models_manager()
        model = manager.load_object("model", level=0)
        self.assertEqual(type(model), type(AffinityPropagation()))

    def test_load_vectorizer(self):
        manager = mock_models_manager()
        vectorizer = manager.load_object("vectorizer", level=0)
        self.assertEqual(type(vectorizer), type(TfidfVectorizer()))

    def test_load_reference_documents_level0(self):
        level = 0
        manager = mock_models_manager()
        reference_documents = manager.load_object("reference_documents", level)
        expected = example_reference_documents[level]
        self.assertEqual(reference_documents, expected)

    def test_load_reference_documents_level1(self):
        level = 1
        manager = mock_models_manager()
        reference_documents = manager.load_object("reference_documents", level)
        expected = example_reference_documents[level]
        self.assertEqual(reference_documents, expected)
