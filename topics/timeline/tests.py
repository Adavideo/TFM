from django.test import TestCase
from .models import Thread, Document
from csv_import.mocks import mock_documents


def validate_thread(test, thread, expected, is_news):
    test.assertEqual(thread.number, expected["thread_number"])
    if is_news:
        test.assertEqual(thread.title, expected["title"])
        test.assertEqual(thread.uri, expected["uri"])

def mock_thread(thread_number, with_documents=False):
    thread = Thread(number=thread_number)
    thread.save()
    if with_documents:
        mock_documents()
        # Assign news
        news = Document.objects.filter(is_news=True)[0]
        thread_info = { "thread_number":thread_number, "title":"", "uri":""}
        news.assign_thread(thread_info)
        # Assign comments
        comments_list = Document.objects.filter(is_news=False)
        for comment in comments_list:
            comment.assign_thread(thread_info)
    return thread


class TheadTests(TestCase):

    def test_create_thread(self):
        thread = mock_thread(thread_number=1)
        self.assertIs(thread.number, 1)
        self.assertEqual(str(thread), "Thread number 1")

    def test_update_thread(self):
        thread = mock_thread(thread_number=1)
        thread.update(title="Title", uri="blabla")
        self.assertIs(thread.title, "Title")
        self.assertIs(thread.uri, "blabla")
        self.assertEqual(str(thread), "Thread number 1 - title: Title")

    def test_news_with_no_news(self):
        thread = mock_thread(thread_number=1, with_documents=False)
        news = thread.news()
        self.assertEqual(news, None)

    def test_news(self):
        thread = thread = mock_thread(thread_number=1, with_documents=True)
        news = thread.news()
        self.assertEqual(news.thread, thread)

    def test_comments_with_no_comments(self):
        thread = Thread(number=1)
        comments = thread.comments()
        self.assertEqual(len(comments), 0)

    def test_comments(self):
        thread = mock_thread(thread_number=1, with_documents=True)
        comments = thread.comments()
        self.assertEqual(len(comments), 5)
        self.assertEqual(comments[1].thread, thread)

    def test_documents_content(self):
        thread = mock_thread(thread_number=1, with_documents=True)
        content_list = thread.documents_content()
        expected_content = example_threads[0]["documents_content"]
        self.assertEqual(len(content_list), len(expected_content))
        self.assertEqual(content_list[0], expected_content[0])
        self.assertEqual(content_list[1], expected_content[1])
        self.assertEqual(content_list[2], expected_content[2])
        validate_documents_content(self, content_list, expected_content)
