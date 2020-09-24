from django.test import TestCase
from joblib import load
from models_generator.ModelsManager import ModelsManager
from testing_commons.mock_documents import mock_documents
from testing_commons.example_documents import example_documents, example_reference_documents
from .validations_models_manager import *
from .load import load_object


class ModelsManagerTests(TestCase):

    def test_get_filename_model(self):
        models_manager = ModelsManager(name="test")
        filename = models_manager.get_filename("model", level=0)
        self.assertEqual(filename, "models/sklearn/test_model_level0.joblib")

    def test_get_filename_vectorizer(self):
        models_manager = ModelsManager(name="test")
        filename = models_manager.get_filename("vectorizer", level=0)
        self.assertEqual(filename, "models/sklearn/test_vectorizer_level0.joblib")

    def test_store_model(self):
        level = 0
        model = load_object("model", level)
        model_name = "delete_me"
        models_manager = ModelsManager(name=model_name)
        models_manager.store_object(model, "model", level)
        validate_model_stored(self, model_name, level)

    def test_store_vectorizer(self):
        level = 0
        vectorizer = load_object("vectorizer", level)
        model_name = "delete_me"
        models_manager = ModelsManager(name=model_name)
        # Execute
        models_manager.store_object(vectorizer, "vectorizer", level)
        # Validate
        validate_vectorizer_stored(self, model_name, level)

    def test_store_reference_documents_level0(self):
        # Initialize
        level = 0
        reference_documents = load_object("reference_documents", level)
        # Execute
        models_manager = ModelsManager(name="delete_me")
        models_manager.store_object(reference_documents, "reference_documents", level)
        # Validate
        expected = example_reference_documents[level]
        validate_reference_documents_stored(self, model_name="delete_me", level=level, expected=expected)

    def test_store_reference_documents_level1(self):
        # Initialize
        level = 1
        reference_documents = load_object("reference_documents", level)
        # Execute
        models_manager = ModelsManager(name="delete_me")
        models_manager.store_object(reference_documents, "reference_documents", level)
        # Validate
        expected = example_reference_documents[level]
        validate_reference_documents_stored(self, model_name="delete_me", level=level, expected=expected)

    def test_generate_and_store_model_level0(self):
        level = 0
        model_name = "delete_me_2"
        models_manager = ModelsManager(name=model_name)
        filenames = models_manager.generate_and_store_models(example_documents, level)
        validate_filenames(self, filenames, name=model_name, num_levels=level+1)
        validate_model_stored(self, model_name, level)
        validate_vectorizer_stored(self, model_name, level)

    def test_generate_and_store_model_level1(self):
        level = 1
        model_name = "delete_me_2"
        mock_documents()
        models_manager = ModelsManager(name=model_name)
        filenames = models_manager.generate_and_store_models(example_documents, level)
        validate_filenames(self, filenames, name=model_name, num_levels=level+1)
        validate_model_stored(self, model_name, level)
        validate_vectorizer_stored(self, model_name, level)
