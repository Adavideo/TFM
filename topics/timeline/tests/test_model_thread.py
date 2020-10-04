from django.test import TestCase
from timeline.models import Thread
from .examples import example_threads
from .mocks import mock_thread
from .validations import validate_thread, validate_content


class ThreadTests(TestCase):

    def test_create_thread(self):
        thread = mock_thread(thread_number=1)
        self.assertIs(thread.number, 1)
        self.assertEqual(str(thread), "Thread number 1")

    def test_update_thread(self):
        thread = mock_thread(thread_number=1)
        title = example_threads[1]["title"]
        uri = example_threads[1]["uri"]
        thread.update(title=title, uri=uri)
        validate_thread(self, thread, example_threads[1], is_news=True)
        self.assertEqual(str(thread), "Thread number 1 - title: "+title)

    def test_news_with_no_news(self):
        thread = mock_thread(thread_number=1, with_documents=False)
        news = thread.news()
        self.assertEqual(news, None)

    def test_news(self):
        thread = mock_thread(thread_number=1, with_documents=True)
        news = thread.news()
        self.assertEqual(news.thread, thread)

    def test_comments_with_no_comments(self):
        thread = Thread(number=1)
        comments = thread.comments()
        self.assertEqual(len(comments), 0)

    def test_comments(self):
        thread = mock_thread(thread_number=1, with_documents=True)
        comments = thread.comments()
        self.assertEqual(len(comments), 2)
        self.assertEqual(comments[1].thread, thread)

    def test_documents_content(self):
        thread = mock_thread(thread_number=1, with_documents=True)
        documents_content = thread.documents_content()
        expected_content = example_threads[1]["documents_content"]
        validate_content(self, documents_content, expected_content)
