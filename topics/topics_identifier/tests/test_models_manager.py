from django.test import TestCase
from sklearn.cluster import AffinityPropagation
from topics_identifier.models_manager import *
from .mocks import mock_documents
from .mock_generators import mock_model
from .examples import example_documents, test_model_name, example_terms


class ModelsManagerTests(TestCase):

    def test_get_filename(self):
        filename = get_filename(name="test", level=0)
        self.assertEqual(filename, "models/sklearn/test_level0.joblib")

    def test_load_model_and_terms(self):
        model, terms = load_model_and_terms(test_model_name, level=0)
        self.assertEqual(type(model), type(AffinityPropagation()))
        self.assertEqual(terms, example_terms)

    def test_load_terms(self):
        terms = load_terms(test_model_name, level=0)
        self.assertEqual(terms, example_terms)

    def test_load_model(self):
        model = load_model(test_model_name, level=0)
        self.assertEqual(type(model), type(AffinityPropagation()))

    def test_store_model(self):
        name = "delete_me"
        level = 0
        model1 = mock_model()
        store_model(model1, name, level)
        model2 = load_model(name, level)
        self.assertEqual(type(model2), type(AffinityPropagation()))

    def test_store_terms(self):
        name = "delete_me"
        level = 0
        store_terms(example_terms, name, level)
        terms = load_terms(name, level)
        self.assertEqual(terms, example_terms)

    def test_select_documents(self):
        document_types = "both"
        mock_documents()
        documents = select_documents(document_types)
        self.assertEqual(documents, example_documents)

    def test_generate_and_store_model(self):
        model_name = "delete_me_2"
        model_filename = generate_and_store_model(model_name, example_documents)
        self.assertEqual(model_filename, "models/sklearn/delete_me_2_level0.joblib")
