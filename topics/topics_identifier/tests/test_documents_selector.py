from django.test import TestCase
from topics_identifier.documents_selector import get_number_of_documents, select_documents
from topics_identifier.models import Document
from .examples import *
from .mocks import mock_news_and_comments
from .validations import validate_documents


class DocumentsSelectorTests(TestCase):

    # get_number_of_documents

    def test_get_number_of_documents_both(self):
        mock_news_and_comments()
        num_documents = get_number_of_documents(documents_types="both")
        self.assertEqual(num_documents, len(all_example_content))

    def test_get_number_of_documents_news(self):
        mock_news_and_comments()
        num_documents = get_number_of_documents(documents_types="news")
        self.assertEqual(num_documents, len(news_content))

    def test_get_number_of_documents_comments(self):
        mock_news_and_comments()
        num_documents = get_number_of_documents(documents_types="comments")
        self.assertEqual(num_documents, len(comments_content))

    # select_documents

    def test_select_documents_news(self):
        documents_types = "news"
        mock_news_and_comments()
        documents_content = select_documents(documents_types, batch_number=1)
        self.assertEqual(documents_content, news_content)

    def test_select_documents_comments_batch1(self):
        documents_types = "comments"
        mock_news_and_comments()
        documents_content = select_documents(documents_types, batch_number=1, size=test_batch_size)
        self.assertEqual(documents_content, comments_content[:test_batch_size])

    def test_select_documents_comments_batch2(self):
        documents_types = "comments"
        mock_news_and_comments()
        documents_content = select_documents(documents_types, batch_number=1, size=test_batch_size)
        self.assertEqual(documents_content, comments_content[:test_batch_size])

    def test_select_documents_both_batch1(self):
        #Initialize
        documents_types = "both"
        mock_news_and_comments()
        #Execute
        batch_documents_content = select_documents(documents_types, batch_number=1, size=test_batch_size)
        #Validate
        expected_content = all_example_content[:test_batch_size]
        self.assertEqual(batch_documents_content, expected_content)

    def test_select_documents_batch2(self):
        #Initialize
        documents_types = "both"
        mock_news_and_comments()
        #Execute
        documents_content = select_documents(documents_types, batch_number=2, size=test_batch_size)
        #Validate
        expected_content = all_example_content[test_batch_size:test_batch_size*2]
        self.assertEqual(documents_content, expected_content)
