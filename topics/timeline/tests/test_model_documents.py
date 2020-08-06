from django.test import TestCase
from .example_documents import example_date, news_content, comments_content
from .mock_documents import mock_document, mock_news, mock_comments
from .test_model_thread import validate_thread
from timeline.models import Document


class DocumentTests(TestCase):

    def test_create_document_news(self):
        doc = mock_news(number=0)
        self.assertEqual(doc.content, news_content[0])
        self.assertIs(doc.is_news, True)
        self.assertEqual(str(doc), "Document 1 - type news, content: "+ news_content[0])

    def test_create_document_comment(self):
        comments = mock_comments()
        self.assertEqual(comments[0].content, comments_content[0])
        self.assertIs(comments[0].is_news, False)
        self.assertEqual(str(comments[0]), "Document 1 - type comment, content: "+ comments_content[0])

    def test_assign_thread_comment(self):
        info = { "thread_number": 10 }
        doc = Document(content="", is_news=False, author=1, date=example_date)
        doc.assign_thread(info)
        self.assertIs(doc.thread.number, 10)

    def test_assign_thread_news(self):
        info = { "thread_number": 10, "title":"example title", "uri":"example uri" }
        doc = Document(content="", is_news=True, author=1, date=example_date)
        doc.assign_thread(info)
        validate_thread(self, doc.thread, info, is_news=True)
