from django.test import TestCase
from sklearn.cluster import AffinityPropagation
from .mock_generators import mock_affinity_propagation_model
from topics_identifier.models_manager import *
from .examples import example_documents
from .mocks import mock_documents


class ModelsManagerTests(TestCase):

    def test_get_filename(self):
        filename = get_filename(name="test", level=0)
        self.assertEqual(filename, "models/sklearn/test_level0.joblib")

    def test_load_model(self):
        name = "test_model"
        model = load_model(name, level=0)
        self.assertEqual(type(model), type(AffinityPropagation()))

    def test_store_model(self):
        name = "test_delete_me"
        level = 0
        model1 = mock_affinity_propagation_model()
        store_model(model1, name, level)
        model2 = load_model(name, level)
        self.assertEqual(type(model2), type(AffinityPropagation()))

    def test_select_documents(self):
        document_types = "both"
        mock_documents()
        documents = select_documents(document_types)
        self.assertEqual(documents, example_documents)

    def test_generate_model(self):
        model = generate_model(example_documents)
        self.assertEqual(type(model), type(AffinityPropagation()))

    def test_generate_and_store_model(self):
        model_name = "test_model2"
        model_filename = generate_and_store_model(model_name, example_documents)
        self.assertEqual(model_filename, "models/sklearn/test_model2_level0.joblib")
