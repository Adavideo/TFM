from django.test import TestCase
from csv_import.csv_importer import get_file_type
from .examples_csv_processed import *


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

    def test_get_file_type_topic_annotations(self):
        header = topic_annotations_header
        result = get_file_type(header)
        self.assertEqual(result, "topic_annotations")
