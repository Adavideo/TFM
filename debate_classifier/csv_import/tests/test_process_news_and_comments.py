from django.test import TestCase
from timeline.models import Thread
from csv_import.csv_importer import *
from .examples_csv_processed import *
from .validations import validate_document_with_thread, validate_processed_line


news = example_processed_news
comment = example_processed_comment


class CSVProcessDataNewsAndCommentsTests(TestCase):

    def test_store_document_news(self):
        store_document(news, is_news=True)
        doc = Document.objects.get(content=news["content"])
        validate_document_with_thread(self, doc, news, is_news=True)

    def test_store_document_adding_news_for_a_thread_that_already_exist(self):
        store_document(comment, is_news=False)
        thread_number = comment["thread_number"]
        thread = Thread.objects.get(number=thread_number)
        self.assertEqual(thread.title, None)
        self.assertEqual(thread.uri, None)
        news["thread_number"] = thread_number
        store_document(news, is_news=True)
        thread = Thread.objects.get(number=thread_number)
        self.assertEqual(thread.title, news["title"])
        self.assertEqual(thread.uri, news["uri"])

    def test_store_document_comment(self):
        store_document(comment, is_news=False)
        doc = Document.objects.get(content=comment["content"])
        validate_document_with_thread(self, doc, comment, is_news=False)

    # Try to store the same document twice
    def test_store_document_twice(self):
        store_document(news, is_news=True)
        store_document(news, is_news=True)
        doc_search = Document.objects.filter(content=news["content"])
        self.assertIs(len(doc_search), 1)

    def test_process_news(self):
        result = process_news(news_example1)
        validate_processed_line(self, result, news, is_news=True)

    def test_process_news_with_quotes(self):
        column = news_example_with_quotes
        result = process_news(column)
        validate_processed_line(self, result, processed_news_with_quotes, is_news=True)

    def test_process_comment(self):
        column = comment_example1
        result = process_comment(column)
        validate_processed_line(self, result, comment, is_news=False)

    def test_process_comment_with_quotes(self):
        column = comment_example_with_quotes
        result = process_comment(column)
        self.assertEqual(result["content"], comment_content_with_quotes)

    def test_process_csv_line_news(self):
        result = process_csv_line(news_example1, file_type="news")
        validate_processed_line(self, result, news, is_news=True)
        doc = Document.objects.get(content=news["content"])
        validate_document_with_thread(self, doc, result, is_news=True)

    def test_process_csv_line_comment(self):
        result = process_csv_line(comment_example1, file_type="comments")
        validate_processed_line(self, result, comment, is_news=False)
        doc = Document.objects.get(content=result["content"])
        validate_document_with_thread(self, doc, result, is_news=False)

    def test_show_progress(self):
        progress = show_progress(num_register=2, total=10)
        expected = "2 of 10 registers. 20.0% completed"
        self.assertEqual(progress, expected)
