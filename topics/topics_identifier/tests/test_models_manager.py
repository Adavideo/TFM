from django.test import TestCase
from sklearn.cluster import AffinityPropagation
from .mock_generators import mock_affinity_propagation_model
from topics_identifier.models_manager import get_filename, store_model, load_model

class ModelsManagerTests(TestCase):

    def test_get_filename(self):
        name = "test"
        filename = get_filename(name)
        self.assertEqual(filename, "models/sklearn/test.joblib")

    def test_load_model(self):
        name = "test_model_level0"
        model = load_model(name)
        self.assertEqual(type(model), type(AffinityPropagation()))

    def test_store_model(self):
        name = "test_delete_me"
        model1 = mock_affinity_propagation_model()
        store_model(model1, name)
        model2 = load_model(name)
        self.assertEqual(type(model2), type(AffinityPropagation()))
