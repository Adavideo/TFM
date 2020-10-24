from django.test import TestCase
from .mocks import *
from .validations import validate_page, validate_threads_list_view

head_text = "Timeline"


class ViewsTests(TestCase):

    def test_timeline_view(self):
        page = 'timeline'
        response = get_response(page)
        validate_page(self, response, head_text)

    def test_threads_list_view_empty(self):
        page = 'threads_list'
        response = get_response(page)
        validate_page(self, response, head_text)

    def test_threads_list_view_with_threads(self):
        page = 'threads_list'
        threads_list = mock_threads_list()
        response = get_response(page)
        validate_page(self, response, head_text)
        validate_threads_list_view(self, response, threads_list)

    def test_thread_view(self):
        page = 'thread'
        thread = mock_thread(thread_number=0, with_documents=True)
        response = get_response(page, arguments=[thread.id])
        validate_page(self, response, head_text)
        self.assertContains(response, thread.title)
        self.assertContains(response, thread.news().content)
        self.assertContains(response, "Comments:")
        for comment in thread.comments():
            self.assertContains(response, comment.content)
            self.assertContains(response, comment.author)

    def test_topics_list_view_empty(self):
        page = 'topics_list'
        response = get_response(page)
        validate_page(self, response, head_text)

    def test_topics_list_view_with_topics(self):
        page = 'topics_list'
        topic0 = mock_topic("topic0")
        topic1 = mock_topic("topic1")
        response = get_response(page)
        validate_page(self, response, head_text)
        self.assertContains(response, topic0.name)
        self.assertContains(response, topic1.name)

    def test_topic_threads_view(self):
        page = 'topic_threads'
        topic = mock_topic()
        threads_list = mock_threads_with_topic(topic)
        response = get_response(page, arguments=[topic.id])
        validate_page(self, response, head_text)
        self.assertContains(response, topic.name)
        validate_threads_list_view(self, response, threads_list)
