from django.test import TestCase
from .examples_csv import *
from topics_identifier.csv_importer import process_news_without_author, process_news_with_author, process_comment


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
