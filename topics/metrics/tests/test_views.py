from django.test import TestCase
from .mocks import *
from .validations_views import *
from .examples_annotations import annotations_examples
from .mock_annotations import mock_topic_annotations, mock_topic_cluster


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

    def test_topic_classification_metrics_view_form(self):
        page = "topic_classification_metrics"
        response = get_response(page)
        validate_page(self, response, head_text)
        self.assertContains(response, "Topic")

    def test_topic_classification_metrics_view_post_no_annotations(self):
        # Initialize
        page = "topic_classification_metrics"
        topic = mock_topic()
        mock_topic_cluster(topic, num_cluster=0)
        parameters = { "topic": topic.id, "model_name": "test" }
        response = post_response(page, parameters)
        # Validate
        validate_page(self, response, head_text)
        self.assertContains(response, "Topic")

    def test_topic_classification_metrics_view_post_small_disagreement(self):
        # Initialize
        page = "topic_classification_metrics"
        topic, annotations_list = mock_topic_annotations(annotations_examples["small disagreement"])
        mock_topic_cluster(topic, num_cluster=0)
        # Execute
        parameters = { "topic": topic.id, "model_name": "test" }
        response = post_response(page, parameters)
        # Validate
        validate_page(self, response, head_text)
        self.assertContains(response, "Topic:</b> "+topic.name)
        self.assertContains(response, "Agreement score:</b> 0.6")
        self.assertContains(response, "Precision:</b> 0.5")
        self.assertContains(response, "Recall:</b> 1")
