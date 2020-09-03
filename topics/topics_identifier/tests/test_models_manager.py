from django.test import TestCase
from sklearn.cluster import AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer
from topics_identifier.ModelsManager import ModelsManager
from .mocks import mock_documents
from .mock_generators import mock_model, mock_models_manager
from .validations_models import *
from .examples import example_documents, test_model_name
from .example_trees import example_tree


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
        validate_reference_documents(self, reference_documents, level, expected)

    def test_load_reference_documents_level1(self):
        level = 1
        manager = mock_models_manager()
        reference_documents = manager.load_object("reference_documents", level)
        expected = example_reference_documents[level]
        validate_reference_documents(self, reference_documents, level, expected)

    def test_store_model(self):
        model_name = "delete_me"
        level = 0
        model = mock_model()
        manager = mock_models_manager(name=model_name)
        manager.store_object(model, "model", level)
        validate_model_stored(self, model_name, level)

    def test_store_vectorizer(self):
        manager1 = mock_models_manager()
        level = 0
        vectorizer = manager1.load_object("vectorizer", level)
        model_name = "delete_me"
        manager2 = mock_models_manager(name=model_name)
        # Execute
        manager2.store_object(vectorizer, "vectorizer", level)
        # Validate
        validate_vectorizer_stored(self, model_name, level)

    def test_store_reference_documents_level0(self):
        # Initialize
        level = 0
        manager_load = mock_models_manager()
        reference_documents = manager_load.load_object("reference_documents", level)
        # Execute
        manager_store = mock_models_manager(name="delete_me")
        manager_store.store_object(reference_documents, "reference_documents", level)
        # Validate
        expected = example_reference_documents[level]
        validate_reference_documents_stored(self, model_name="delete_me", level=level, expected=expected)

    def test_store_reference_documents_level1(self):
        # Initialize
        level = 1
        manager_load = mock_models_manager()
        reference_documents = manager_load.load_object("reference_documents", level)
        # Execute
        manager_store = mock_models_manager(name="delete_me")
        manager_store.store_object(reference_documents, "reference_documents", level)
        # Validate
        expected = example_reference_documents[level]
        validate_reference_documents_stored(self, model_name="delete_me", level=level, expected=expected)

    def test_generate_and_store_model_level0(self):
        level = 0
        model_name = "delete_me_2"
        manager = mock_models_manager(name=model_name)
        model_filename = manager.generate_and_store_models(example_documents, level)
        self.assertEqual(model_filename, "models/sklearn/delete_me_2_model_level0.joblib")
        validate_model_stored(self, model_name, level)
        validate_vectorizer_stored(self, model_name, level)

    def test_generate_and_store_model_level1(self):
        level = 1
        model_name = "delete_me_2"
        mock_documents()
        manager = mock_models_manager(name=model_name)
        model_filename = manager.generate_and_store_models(example_documents, level)
        self.assertEqual(model_filename, "models/sklearn/delete_me_2_model_level1.joblib")
        validate_model_stored(self, model_name, level)
        validate_vectorizer_stored(self, model_name, level)
