from django.test import TestCase
from topics_identifier.datasets_manager import *
from .examples import example_documents, news_content, comments_content, all_threads_content
from .example_trees import example_tree
from .mocks import mock_documents, mock_news, mock_comments, mock_thread
from .mock_trees import mock_tree
from .validations_documents import validate_documents_content
from .examples import all_threads_content, example_threads


def validate_dataset(test, dataset, expected_content):
    test.assertEqual(str(type(dataset)), "<class 'sklearn.utils.Bunch'>")
    validate_documents_content(test, dataset.data, expected_content)


class DatasetManagerTests(TestCase):

    def test_select_documents_level0_news(self):
        mock_news(number=0)
        mock_news(number=1)
        mock_comments()
        expected_content = [ news_content[0], news_content[1] ]
        documents_content = select_documents_level0(news=True, comments=False)
        validate_documents_content(self, documents_content, expected_content)

    def test_select_documents_level0_comments(self):
        mock_news(number=0)
        mock_news(number=1)
        mock_comments()
        documents_content = select_documents_level0(news=False, comments=True)
        validate_documents_content(self, documents_content, comments_content)

    def test_select_documents_level0_both(self):
        mock_news(number=0)
        mock_news(number=1)
        mock_comments()
        expected_content = [ news_content[0], news_content[1] ]
        expected_content.extend(comments_content)
        documents_content = select_documents_level0(news=True, comments=True)
        validate_documents_content(self, documents_content, expected_content)

    def test_generate_dataset(self):
        dataset = generate_dataset(example_documents)
        validate_dataset(self, dataset, example_documents)

    def test_get_dataset_level0(self):
        mock_documents()
        tree = mock_tree()
        dataset = get_dataset(tree, level=0)
        validate_dataset(self, dataset, example_documents)

    def test_get_dataset_level1(self):
        level = 1
        mock_documents()
        tree = mock_tree(level, linked=True)
        dataset = get_dataset(tree, level)
        documents_level1 = example_tree[1]["documents"]
        validate_dataset(self, dataset, documents_level1)

    def test_generate_dataset_from_threads_one_thread(self):
        thread0 = mock_thread(thread_number=0, with_documents=True, news_number=0)
        threads_list = [ thread0 ]
        dataset = generate_dataset_from_threads(threads_list)
        expected_content = example_threads[0]["documents_content"]
        validate_dataset(self, dataset, expected_content)

    def test_generate_dataset_from_threads_two_threads(self):
        thread0 = mock_thread(thread_number=0, with_documents=True, news_number=0)
        thread1 = mock_thread(thread_number=1, with_documents=True, news_number=1)
        threads_list = [ thread0, thread1 ]
        dataset = generate_dataset_from_threads(threads_list)
        validate_dataset(self, dataset, all_threads_content)
