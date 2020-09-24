from django.test import TestCase
from testing_commons.example_documents import *
from testing_commons.mock_documents import mock_news_and_comments, mock_documents
from testing_commons.validations_documents import validate_documents
from timeline.models import Document
from models_generator.documents_selector import *
from .examples import example_max_documents


def expected_content_all():
    expected_content = [ news_content[0], news_content[1] ]
    expected_content.extend(comments_content)
    return expected_content


class DocumentsSelectorTests(TestCase):

    def test_short_document_types_both(self):
        news, comments = short_document_types(document_types="both")
        self.assertEqual(news, True)
        self.assertEqual(comments, True)

    def test_short_document_types_news(self):
        news, comments = short_document_types(document_types="news")
        self.assertEqual(news, True)
        self.assertEqual(comments, False)

    def test_short_document_types_comments(self):
        news, comments = short_document_types(document_types="comments")
        self.assertEqual(news, False)
        self.assertEqual(comments, True)

    def test_ensure_documents_limit(self):
        documents1 = example_documents
        self.assertEqual(len(documents1), 10)
        limit = 5
        documents2 = ensure_documents_limit(documents1, limit)
        self.assertEqual(len(documents2), 5)
        self.assertEqual(documents1[:limit], documents2)

    def test_select_documents_from_database_news(self):
        document_types = "news"
        mock_news_and_comments()
        expected_content = [ news_content[0], news_content[1] ]
        documents_list = select_documents_from_database(document_types)
        validate_documents(self, documents_list, expected_content)

    def test_select_documents_from_database_comments(self):
        document_types="comments"
        mock_news_and_comments()
        documents_content = select_documents_from_database(document_types)
        validate_documents(self, documents_content, example_documents)

    def test_select_documents_from_database_both(self):
        document_types="both"
        mock_news_and_comments()
        expected_content = expected_content_all()
        documents_content = select_documents_from_database(document_types)
        validate_documents(self, documents_content, expected_content)

    def test_get_documents_content(self):
        mock_news_and_comments()
        expected_content = expected_content_all()
        documents_list = Document.objects.all()
        documents_content = get_documents_content(documents_list)
        self.assertEqual(documents_content, expected_content)

    def test_select_documents(self):
        mock_news_and_comments()
        expected_content = expected_content_all()
        documents_content = select_documents(document_types="both", max_num_documents=example_max_documents)
        self.assertEqual(documents_content, expected_content)

    def test_select_documents_with_max_num_documents(self):
        mock_news_and_comments()
        documents_content = select_documents(document_types="both", max_num_documents=5)
        expected_content = expected_content_all()
        self.assertEqual(len(documents_content), 5)
        self.assertEqual(documents_content, expected_content[:5])
