from django.test import TestCase
from topics_identifier.datasets_manager import generate_dataset, select_documents_level0, get_dataset
from .examples import example_documents, example_tree
from .mocks import mock_tree
from csv_import.mocks import mock_documents
from .validations import validate_documents_content


class DatasetManagerTests(TestCase):

    def test_select_documents_level0_news(self):
        mock_documents()
        documents_content = select_documents_level0(news=True, comments=False)
        validate_documents_content(self, documents_content, example_documents, document_types="news")

    def test_select_documents_level0_comments(self):
        mock_documents()
        documents_content = select_documents_level0(news=False, comments=True)
        validate_documents_content(self, documents_content, example_documents, document_types="comments")

    def test_select_documents_level0_both(self):
        mock_documents()
        documents_content = select_documents_level0(news=True, comments=True)
        validate_documents_content(self, documents_content, example_documents)

    def test_generate_dataset(self):
        dataset = generate_dataset(example_documents)
        self.assertEqual(str(type(dataset)), "<class 'sklearn.utils.Bunch'>")
        validate_documents_content(self, dataset.data, example_documents)

    def test_get_dataset_level0(self):
        mock_documents()
        tree = mock_tree()
        dataset = get_dataset(tree, level=0)
        self.assertEqual(str(type(dataset)), "<class 'sklearn.utils.Bunch'>")
        validate_documents_content(self, dataset.data, example_documents)

    def test_get_dataset_level1(self):
        level = 1
        mock_documents()
        tree = mock_tree(level, linked=True)
        dataset = get_dataset(tree, level)
        documents_level1 = example_tree[1]["documents"]
        self.assertEqual(str(type(dataset)), "<class 'sklearn.utils.Bunch'>")
        validate_documents_content(self, dataset.data, documents_level1)
