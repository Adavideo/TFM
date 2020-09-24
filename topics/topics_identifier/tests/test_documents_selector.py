from django.test import TestCase
from topics_identifier.documents_selector import *
from topics_identifier.models import Document
from .examples_documents_selector import example_doc_options, doc_options_with_batches
from .example_documents import *
from .examples import test_batch_size, example_threads
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

    def test_get_number_of_documents_no_batches(self):
        mock_documents()
        options = { "types":"both", "max_num_documents": None, "batches": False }
        num_documents = get_number_of_documents(options)
        self.assertEqual(num_documents, len(example_documents))

    def test_get_number_of_documents_with_batches(self):
        mock_documents()
        options = { "types":"both", "max_num_documents": None, "batches": True }
        num_documents = get_number_of_documents(options)
        self.assertEqual(num_documents, len(example_documents))

    def test_get_number_of_documents_news(self):
        mock_news_and_comments()
        options = { "types":"news", "max_num_documents": None, "batches": True }
        num_documents = get_number_of_documents(options)
        self.assertEqual(num_documents, len(news_content))

    def test_get_number_of_documents_comments(self):
        mock_news_and_comments()
        options = { "types":"comments", "max_num_documents": None, "batches": True }
        num_documents = get_number_of_documents(options)
        self.assertEqual(num_documents, len(comments_content))

    def test_get_documents_content(self):
        mock_news_and_comments()
        expected_content = expected_content_all()
        documents_list = Document.objects.all()
        documents_content = get_documents_content(documents_list)
        self.assertEqual(documents_content, expected_content)

    def test_get_documents_batch_1(self):
        #Initialize
        batch_number = 1
        batch_options = { "size": test_batch_size, "number": batch_number }
        mock_documents()
        document_list = Document.objects.all()
        #Execute
        batch = get_documents_batch(document_list, batch_options)
        #Validate
        self.assertEqual(len(batch), test_batch_size)
        expected = document_list[:test_batch_size]
        for i in range(len(batch)):
            self.assertEqual( batch[i], expected[i])

    def test_get_documents_batch_2(self):
        #Initialize
        batch_options = { "size": test_batch_size, "number": 2 }
        mock_documents()
        document_list = Document.objects.all()
        #Execute
        batch = get_documents_batch(document_list, batch_options)
        #Validate
        self.assertEqual(len(batch), test_batch_size)
        expected = document_list[test_batch_size:test_batch_size*2]
        for i in range(len(batch)):
            self.assertEqual(batch[i], expected[i])

    def test_select_documents_no_batch(self):
        mock_news_and_comments()
        expected_content = expected_content_all()
        documents_content = select_documents(example_doc_options)
        self.assertEqual(documents_content, expected_content)

    def test_select_documents_batch1(self):
        #Initialize
        mock_news_and_comments()
        batch_options = { "size": test_batch_size, "number": 1 }
        #Execute
        documents_content = select_documents(doc_options_with_batches, batch_options)
        #Validate
        expected_content = expected_content_all()[:test_batch_size]
        self.assertEqual(documents_content, expected_content)

    def test_select_documents_batch2(self):
        #Initialize
        mock_news_and_comments()
        batch_options = { "size": test_batch_size, "number": 2 }
        #Execute
        documents_content = select_documents(doc_options_with_batches, batch_options)
        #Validate
        expected_content = expected_content_all()[test_batch_size:test_batch_size*batch_options["number"]]
        self.assertEqual(documents_content, expected_content)

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
