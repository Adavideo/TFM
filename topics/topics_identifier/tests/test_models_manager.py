from django.test import TestCase
from sklearn.cluster import AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer
from topics_identifier.models_manager import *
from .mocks import mock_documents
from .mock_generators import mock_model
from .validations_models import *
from .examples import example_documents, test_model_name, example_terms


class ModelsManagerTests(TestCase):

    def test_get_model_filename(self):
        filename = get_model_filename(name="test", level=0)
        self.assertEqual(filename, "models/sklearn/test_model_level0.joblib")

    def test_get_vectorizer_filename(self):
        filename = get_vectorizer_filename(name="test", level=0)
        self.assertEqual(filename, "models/sklearn/test_vectorizer_level0.joblib")

    def test_load_model(self):
        model = load_model(test_model_name, level=0)
        self.assertEqual(type(model), type(AffinityPropagation()))

    def test_load_vectorizer(self):
        vectorizer = load_vectorizer(test_model_name, level=0)
        self.assertEqual(type(vectorizer), type(TfidfVectorizer()))

    def test_load_model_and_vectorizer(self):
        model, vectorizer = load_model_and_vectorizer(test_model_name, level=0)
        self.assertEqual(type(model), type(AffinityPropagation()))
        self.assertEqual(type(vectorizer), type(TfidfVectorizer()))

    def test_store_model(self):
        store_name = "delete_me"
        level = 0
        model1 = mock_model()
        store_model(model1, store_name, level)
        validate_model_stored(self, store_name, level)

    def test_store_vectorizer(self):
        store_name = "delete_me"
        level = 0
        vectorizer1 = load_vectorizer(test_model_name, level)
        store_vectorizer(vectorizer1, store_name, level)
        validate_vectorizer_stored(self, store_name, level)

    def test_select_documents(self):
        document_types = "both"
        mock_documents()
        documents = select_documents(document_types)
        self.assertEqual(documents, example_documents)

    def test_generate_and_store_model(self):
        model_name = "delete_me_2"
        model_filename = generate_and_store_model(model_name, example_documents)
        self.assertEqual(model_filename, "models/sklearn/delete_me_2_model_level0.joblib")
