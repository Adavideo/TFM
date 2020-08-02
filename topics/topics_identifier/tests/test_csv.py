from django.test import TestCase
from .examples_csv import *
from .examples import example_documents
from topics_identifier.csv_importer import *


class CSVProcessDataTests(TestCase):

    def test_store_document_news(self):
        text = example_documents[0]
        file_type = "news"
        store_document(text, file_type)
        doc = Document.objects.get(content=text)
        self.assertEqual(doc.content, text)
        self.assertEqual(doc.news, True)

    def test_store_document_comment(self):
        text = example_documents[0]
        file_type = "comments"
        store_document(text, file_type)
        doc = Document.objects.get(content=text)
        self.assertEqual(doc.content, text)
        self.assertEqual(doc.news, False)

    # Try to store the same document twice
    def test_store_document_twice(self):
        text = example_documents[0]
        file_type = "news"
        store_document(text, file_type)
        store_document(text, file_type)
        doc_search = Document.objects.filter(content=text)
        self.assertIs(len(doc_search), 1)

    def test_process_news(self):
        column = news_example1
        result = process_news(column)
        self.assertEqual(result["title"], news_title1)
        self.assertEqual(result["content"], news_content1)

    def test_process_news_with_quotes(self):
        column = news_example_with_quotes
        result = process_news(column)
        self.assertEqual(result["title"], news_title_with_quotes)
        self.assertEqual(result["content"], news_content_with_quotes)

    def test_process_comment(self):
        column = comment_example1
        result = process_comment(column)
        self.assertEqual(result["content"], comment_content1)

    def test_process_comment_with_quotes(self):
        column = comment_example_with_quotes
        result = process_comment(column)
        self.assertEqual(result["content"], comment_content_with_quotes)

    def test_process_csv_line_news(self):
        file_type = "news"
        column = news_example1
        result = process_csv_line(column, file_type)
        self.assertEqual(result["title"], news_title1)
        self.assertEqual(result["content"], news_content1)
        text = news_example1[5] + "\n" + news_example1[6]
        doc = Document.objects.get(content=text)
        self.assertEqual(doc.content, text)

    def test_process_csv_line_comment(self):
        file_type = "comments"
        column = comment_example1
        result = process_csv_line(column, file_type)
        self.assertEqual(result["content"], comment_content1)
        text = comment_example1[4]
        doc = Document.objects.get(content=text)
        self.assertEqual(doc.content, text)

    def test_show_progress(self):
        progress = show_progress(num_register=2, total=10)
        expected = "2 of 10 registers. 20.0% completed"
        self.assertEqual(progress, expected)


class CSVImporterTests(TestCase):

    def test_get_file_type_incorrect_header(self):
        header = incorrect_header_example
        result = get_file_type(header)
        self.assertEqual(result, "incorrect")

    def test_get_file_type_news(self):
        header = news_header
        result = get_file_type(header)
        self.assertEqual(result, "news")

    def test_get_file_type_comments(self):
        header = comments_header
        result = get_file_type(header)
        self.assertEqual(result, "comments")
