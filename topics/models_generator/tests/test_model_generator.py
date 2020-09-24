from django.test import TestCase
from testing_commons.example_documents import example_documents, example_reference_documents
from models_generator.ModelsManager import ModelsManager
from .validations_models_manager import *


class ModelGeneratorTests(TestCase):

    def test_generate_model_level0(self):
        level = 0
        model_name = "delete_me_3"
        models_manager = ModelsManager(name=model_name)
        models_manager.generate_and_store_models(documents=example_documents, max_level=level)
        validate_model_stored(self, model_name, level)
        validate_vectorizer_stored(self, model_name, level)
        expected = example_reference_documents[level]
        validate_reference_documents_stored(self, model_name, level, expected)

    def test_generate_model_level1(self):
        level = 1
        model_name = "delete_me_3"
        manager_manager = ModelsManager(name=model_name)
        manager_manager.generate_and_store_models(documents=example_documents, max_level=level)
        validate_model_stored(self, model_name, level)
        validate_vectorizer_stored(self, model_name, level)
        expected = example_reference_documents[level]
        validate_reference_documents_stored(self, model_name, level, expected)
