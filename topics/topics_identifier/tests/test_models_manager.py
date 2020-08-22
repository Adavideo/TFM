from django.test import TestCase
from sklearn.cluster import AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer
from topics_identifier.ModelsManager import ModelsManager
from .mocks import mock_documents
from .mock_generators import mock_model, mock_models_manager
from .validations_models import *
from .examples import example_documents, test_model_name

manager = mock_models_manager()

class ModelsManagerTests(TestCase):

    def test_get_model_filename(self):
        manager2 = mock_models_manager(name="test")
        filename = manager2.get_model_filename( level=0)
        self.assertEqual(filename, "models/sklearn/test_model_level0.joblib")

    def test_get_vectorizer_filename(self):
        manager2 = mock_models_manager(name="test")
        filename = manager2.get_vectorizer_filename(level=0)
        self.assertEqual(filename, "models/sklearn/test_vectorizer_level0.joblib")

    def test_load_model(self):
        model = manager.load_model(level=0)
        self.assertEqual(type(model), type(AffinityPropagation()))

    def test_load_vectorizer(self):
        vectorizer = manager.load_vectorizer(level=0)
        self.assertEqual(type(vectorizer), type(TfidfVectorizer()))

    def test_store_model(self):
        model_name = "delete_me"
        level = 0
        model = mock_model()
        manager3 = mock_models_manager(name=model_name)
        manager3.store_model(model, level)
        validate_model_stored(self, model_name, level)

    def test_store_vectorizer(self):
        model_name = "delete_me"
        level = 0
        vectorizer = manager.load_vectorizer(level)
        manager3 = mock_models_manager(name=model_name)
        manager3.store_vectorizer(vectorizer, level)
        validate_vectorizer_stored(self, model_name, level)

    def test_generate_and_store_model_level0(self):
        level = 0
        model_name = "delete_me_2"
        manager4 = mock_models_manager(name=model_name)
        model_filename = manager4.generate_and_store_models(example_documents, level)
        self.assertEqual(model_filename, "models/sklearn/delete_me_2_model_level0.joblib")
        validate_model_stored(self, model_name, level)
        validate_vectorizer_stored(self, model_name, level)

    def test_generate_and_store_model_level1(self):
        level = 1
        model_name = "delete_me_2"
        manager4 = mock_models_manager(name=model_name)
        model_filename = manager4.generate_and_store_models(example_documents, level)
        self.assertEqual(model_filename, "models/sklearn/delete_me_2_model_level1.joblib")
        validate_model_stored(self, model_name, level)
        validate_vectorizer_stored(self, model_name, level)
