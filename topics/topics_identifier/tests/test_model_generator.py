from django.test import TestCase
from .mock_generators import mock_models_manager
from .validations_models import *
from .examples_models import test_model_name
from .example_documents import example_documents
from .examples_documents_selector import example_documents_limit
from .example_trees import example_tree


class ModelGeneratorTests(TestCase):

    def test_generate_model_level0(self):
        level = 0
        model_name = "delete_me_3"
        models_manager = mock_models_manager(name=model_name)
        models_manager.generate_and_store_models(documents=example_documents, max_level=level)
        validate_model_stored(self, model_name, level)
        validate_vectorizer_stored(self, model_name, level)
        expected = example_tree[level]["reference_documents"]
        validate_reference_documents_stored(self, model_name, level, expected)

    def test_generate_model_level1(self):
        level = 1
        model_name = "delete_me_3"
        manager_manager = mock_models_manager(name=model_name)
        manager_manager.generate_and_store_models(documents=example_documents, max_level=level)
        validate_model_stored(self, model_name, level)
        validate_vectorizer_stored(self, model_name, level)
        expected = example_tree[level]["reference_documents"]
        validate_reference_documents_stored(self, model_name, level, expected)
