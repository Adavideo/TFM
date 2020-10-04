from django.test import TestCase
from .mocks import *
from .validations_views import *

head_text = "Metrics"


class ViewsTests(TestCase):

    def test_home_page(self):
        page = 'metrics'
        response = get_response(page)
        validate_page(self, response, head_text)

    def test_generate_sample_view_form(self):
        page = "generate_sample"
        response = get_response(page)
        validate_page(self, response, head_text)

    def test_generate_sample_view_post(self):
        page = "generate_sample"
        topic = mock_threads_and_clusters_with_topic()
        parameters = { "topic": topic.id, "filename": "test_sample" }
        #Execute
        response = post_response(page, parameters)
        #Validate
        validate_page(self, response, head_text)
