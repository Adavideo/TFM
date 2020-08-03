from django.test import TestCase
from topics_identifier.models import Document
from .examples import example_documents, example_date
from .mocks import mock_document
from timeline.tests import validate_thread


class DocumentTests(TestCase):

    def test_create_document_news(self):
        content = example_documents[2]
        doc = mock_document(content=content, is_news=True)
        doc.save()
        self.assertEqual(doc.content, example_documents[2])
        self.assertIs(doc.is_news, True)
        self.assertEqual(str(doc), "Document 1 - type news, content: "+ example_documents[2])

    def test_create_document_comment(self):
        content = example_documents[0]
        doc = mock_document(content=content, is_news=False)
        doc.save()
        self.assertEqual(doc.content, example_documents[0])
        self.assertIs(doc.is_news, False)
        self.assertEqual(str(doc), "Document 1 - type comment, content: "+ example_documents[0])

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
