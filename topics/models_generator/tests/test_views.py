from django.test import TestCase
from common.testing.mock_documents import mock_documents
from common.testing.mock_web_client import get_response, post_response
from .validations_views import *

page = 'generate_models'
head_text = "Generate model"


class ViewsTests(TestCase):

    def test_generate_model_view_form(self):
        response = get_response(page)
        validate_page(self, response, head_text)
        self.assertContains(response, "Model name")
        self.assertContains(response, "Document types")
        self.assertContains(response, "Max number of documents")
        self.assertContains(response, "Max tree level")

    def test_generate_model_view_post_level0(self):
        #Initialize
        name = "delete_me_generate_model_test"
        max_level = 0
        parameters = { "model_name": name, "document_types":"both",
                       "max_num_documents": 100, "max_level": max_level }
        mock_documents()
        #Execute
        response = post_response(page, parameters)
        #Validate
        validate_generate_model_view(self, response, name, max_level)

    def test_generate_model_view_post_level1(self):
        #Initialize
        name = "delete_me_generate_model_test"
        max_level = 1
        parameters = { "model_name": name, "document_types":"both",
                       "max_num_documents": 100, "max_level": max_level }
        mock_documents()
        #Execute
        response = post_response(page, parameters)
        #Validate
        validate_generate_model_view(self, response, name, max_level)
