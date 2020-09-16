from django.test import TestCase
from topics_identifier.documents_selector import *
from .examples_documents_selector import *
from .example_documents import *
from .examples import example_threads
from .mocks import mock_thread
from .mock_documents import mock_news_and_comments, mock_documents
from .validations_documents import validate_documents


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
        documents_options = { "types": "news"}
        mock_news_and_comments()
        expected_content = [ news_content[0], news_content[1] ]
        documents_list = select_documents_from_database(documents_options)
        validate_documents(self, documents_list, expected_content)

    def test_select_documents_from_database_comments(self):
        documents_options = { "types": "comments"}
        mock_news_and_comments()
        documents_content = select_documents_from_database(documents_options)
        validate_documents(self, documents_content, example_documents)

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
        self.assertEqual(documents_content, expected_content)

    def test_select_documents(self):
        mock_news_and_comments()
        expected_content = expected_content_all()
        documents_content = select_documents(documents_options=example_doc_options)
        self.assertEqual(documents_content, expected_content)

    def test_select_documents_max_num_documents(self):
        mock_news_and_comments()
        documents_options = { "types": "both", "max_num_documents":5 }
        documents_content = select_documents(documents_options)
        expected_content = expected_content_all()
        self.assertEqual(len(documents_content), 5)
        self.assertEqual(documents_content, expected_content[:5])

    def test_get_documents_from_threads_one_thread(self):
        thread0 = mock_thread(thread_number=0, with_documents=True, news_number=0)
        threads_list = [ thread0 ]
        documents = get_documents_from_threads(threads_list)
        expected_content = example_threads[0]["documents_content"]
        self.assertEqual(documents, expected_content)

    def test_get_documents_from_threads_two_threads(self):
        thread0 = mock_thread(thread_number=0, with_documents=True, news_number=0)
        thread1 = mock_thread(thread_number=1, with_documents=True, news_number=1)
        threads_list = [ thread0, thread1 ]
        documents = get_documents_from_threads(threads_list)
        self.assertEqual(documents, all_threads_content)
