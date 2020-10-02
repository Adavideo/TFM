from django.test import TestCase
from common.testing.example_documents import *
from common.testing.mock_documents import mock_news_and_comments, mock_documents
from common.testing.validations_documents import validate_documents
from timeline.models import Document
from models_generator.documents_selector import *
from .examples import example_max_documents


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
        document_types = "news"
        mock_news_and_comments()
        expected_content = [ news_content[0], news_content[1] ]
        documents_list = select_documents_from_database(document_types)
        validate_documents(self, documents_list, expected_content)

    def test_select_documents_from_database_comments(self):
        document_types="comments"
        mock_news_and_comments()
        selected_documents = select_documents_from_database(document_types)
        validate_documents(self, selected_documents, comments_content)

    def test_select_documents_from_database_both(self):
        document_types="both"
        expected_documents = mock_news_and_comments()
        selected_documents = select_documents_from_database(document_types)
        for i in range(len(expected_documents)):
            self.assertEqual(selected_documents[i], expected_documents[i])

    def test_get_documents_content(self):
        all_documents = mock_news_and_comments()
        expected_content = [ doc.content for doc in all_documents ]
        documents_list = Document.objects.all()
        documents_content = get_documents_content(documents_list)
        self.assertEqual(documents_content, expected_content)

    def test_select_documents(self):
        all_documents = mock_news_and_comments()
        expected_content = [ doc.content for doc in all_documents ]
        documents_content = select_documents(document_types="both", max_num_documents=100)
        self.assertEqual(documents_content, expected_content)

    def test_select_documents_with_max_num_documents(self):
        all_documents = mock_news_and_comments()
        expected_content = [ doc.content for doc in all_documents ]
        documents_content = select_documents(document_types="both", max_num_documents=example_max_documents)
        self.assertEqual(len(documents_content), example_max_documents)
        self.assertEqual(documents_content, expected_content[:example_max_documents])
