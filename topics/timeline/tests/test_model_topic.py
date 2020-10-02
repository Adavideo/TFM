from django.test import TestCase
from timeline.models import Topic
from .examples import all_threads_content, threads_news, threads_comments
from .mocks import mock_topic, mock_threads_with_topic
from .validations import validate_documents_content


class TopicTests(TestCase):

    def test_get_threads(self):
        topic = mock_topic()
        mocked_threads = mock_threads_with_topic(topic)
        threads_list = topic.get_threads()

    def test_get_labeled_documents_both(self):
        topic = mock_topic()
        mock_threads_with_topic(topic)
        documents = topic.get_documents()
        validate_documents_content(self, documents, all_threads_content)

    def test_get_labeled_documents_news(self):
        topic = mock_topic()
        mock_threads_with_topic(topic)
        documents = topic.get_documents(type="news")
        validate_documents_content(self, documents, threads_news)

    def test_get_labeled_documents_comments(self):
        topic = mock_topic()
        mock_threads_with_topic(topic)
        documents = topic.get_documents(type="comments")
        validate_documents_content(self, documents, threads_comments)
