from django.test import TestCase
from topics_identifier.models_manager import generate_and_store_models
from .validations_models import validate_model_stored, validate_vectorizer_stored
from .examples import test_model_name, example_documents


class ModelGeneratorTests(TestCase):

    def test_generate_model_level0(self):
        level = 0
        model_name = "delete_me_model_generator"
        generate_and_store_models(model_name=model_name, documents=example_documents, max_level=level)
        validate_model_stored(self, test_model_name, level)
        validate_vectorizer_stored(self, test_model_name, level)

    def test_generate_model_level1(self):
        level = 1
        model_name = "delete_me_model_generator"
        generate_and_store_models(model_name=model_name, documents=example_documents, max_level=level)
        validate_model_stored(self, test_model_name, level)
        validate_vectorizer_stored(self, test_model_name, level)
