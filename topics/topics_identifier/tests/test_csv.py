from django.test import TestCase
from .examples_csv import *
from topics_identifier.csv_importer import process_news_without_author, process_news_with_author, process_comment, process_csv_line, get_file_type


class CSVProcessDataTests(TestCase):

    def test_news_without_author(self):
        column = news_without_author_example1
        result = process_news_without_author(column)
        self.assertEqual(result["title"], news_without_author_title1)
        self.assertEqual(result["content"], news_without_author_content1)

    def test_news_with_author(self):
        column = news_with_author_example1
        result = process_news_with_author(column)
        self.assertEqual(result["title"], news_with_author_title1)
        self.assertEqual(result["content"], news_with_author_content1)

    def test_comment(self):
        column = comment_example1
        result = process_comment(column)
        self.assertEqual(result["content"], comment_content1)

    def test_process_csv_line_news_without_author(self):
        file_type = "news_without_author"
        column = news_without_author_example1
        result = process_csv_line(column, file_type)
        self.assertEqual(result["title"], news_without_author_title1)
        self.assertEqual(result["content"], news_without_author_content1)

    def test_process_csv_line_news_with_author(self):
        file_type = "news_with_author"
        column = news_with_author_example1
        result = process_csv_line(column, file_type)
        self.assertEqual(result["title"], news_with_author_title1)
        self.assertEqual(result["content"], news_with_author_content1)

    def test_process_csv_line_comment(self):
        file_type = "comments"
        column = comment_example1
        result = process_csv_line(column, file_type)
        self.assertEqual(result["content"], comment_content1)


class CSVImporterTests(TestCase):

    def test_get_file_type_incorrect_header(self):
        header = incorrect_header_example
        result = get_file_type(header)
        self.assertEqual(result, "incorrect")
