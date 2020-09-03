from django.test import TestCase
from .mock_generators import mock_models_manager
from .validations_models import validate_model_stored, validate_vectorizer_stored
from .examples import test_model_name, example_documents, example_documents_limit


class ModelGeneratorTests(TestCase):

    def test_generate_model_level0(self):
        level = 0
        model_name = "delete_me_3"
        manager = mock_models_manager(name=model_name)
        manager.generate_and_store_models(documents=example_documents, max_level=level)
        validate_model_stored(self, model_name, level)
        validate_vectorizer_stored(self, model_name, level)

    def test_generate_model_level1(self):
        level = 1
        model_name = "delete_me_3"
        manager = mock_models_manager(name=model_name)
        manager.generate_and_store_models(documents=example_documents, max_level=level)
        validate_model_stored(self, model_name, level)
        validate_vectorizer_stored(self, model_name, level)
