from django.test import TestCase
from .examples import *
from topics_identifier.csv_importer import process_news_without_author, get_file_type


class CSVProcessDataTests(TestCase):

    def test_news_without_author(self):
        column = news_without_author_example1
        result = process_news_without_author(column)
        expected_result = "title: " + news_without_author_title1 + "\ncontent: " + news_without_author_content1
        self.assertEqual(result, expected_result)
