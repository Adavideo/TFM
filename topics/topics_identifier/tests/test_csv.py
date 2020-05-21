from django.test import TestCase
from .examples_csv import *
from topics_identifier.csv_importer import process_news, process_comment, process_csv_line, get_file_type


class CSVProcessDataTests(TestCase):

    def test_news(self):
        column = news_example1
        result = process_news(column)
        self.assertEqual(result["title"], news_title1)
        self.assertEqual(result["content"], news_content1)

    def test_news_with_quotes(self):
        column = news_example_with_quotes
        result = process_news(column)
        self.assertEqual(result["title"], news_title_with_quotes)
        self.assertEqual(result["content"], news_content_with_quotes)

    def test_comment(self):
        column = comment_example1
        result = process_comment(column)
        self.assertEqual(result["content"], comment_content1)

    def test_comment_with_quotes(self):
        column = comment_example_with_quotes
        result = process_comment(column)
        self.assertEqual(result["content"], comment_content_with_quotes)

    def test_process_csv_line_news(self):
        file_type = "news"
        column = news_example1
        result = process_csv_line(column, file_type, count=1)
        self.assertEqual(result["title"], news_title1)
        self.assertEqual(result["content"], news_content1)

    def test_process_csv_line_comment(self):
        file_type = "comments"
        column = comment_example1
        result = process_csv_line(column, file_type, count=2)
        self.assertEqual(result["content"], comment_content1)


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
