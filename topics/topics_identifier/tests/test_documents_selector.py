from django.test import TestCase
from topics_identifier.documents_selector import *
from .examples import news_content, comments_content, example_doc_options
from .mocks import mock_news_and_comments
from .validations_documents import validate_documents, validate_documents_content


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

    def test_select_documents_from_database_news(self):
        documents_options = { "types": "news"}
        mock_news_and_comments()
        expected_content = [ news_content[0], news_content[1] ]
        documents_list = select_documents_from_database(documents_options)
        validate_documents(self, documents_list, expected_content)

    def test_select_documents_from_database_comments(self):
        documents_options = { "types": "comments"}
        mock_news_and_comments()
        documents_content = select_documents_from_database(documents_options)
        validate_documents(self, documents_content, comments_content)

    def test_select_documents_from_database_both(self):
        documents_options = { "types": "both"}
        mock_news_and_comments()
        expected_content = expected_content_all()
        documents_content = select_documents_from_database(documents_options)
        validate_documents(self, documents_content, expected_content)

    def test_get_documents_content(self):
        mock_news_and_comments()
        expected_content = expected_content_all()
        documents_list = Document.objects.all()
        documents_content = get_documents_content(documents_list)
        validate_documents_content(self, documents_content, expected_content)

    def test_select_documents(self):
        mock_news_and_comments()
        expected_content = expected_content_all()
        documents_content = select_documents(documents_options=example_doc_options, limit=100, topic=None)
        validate_documents_content(self, documents_content, expected_content)
