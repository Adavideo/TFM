from django.test import TestCase
from topics_identifier.datasets_manager import generate_dataset, generate_dataset_from_threads
from .examples import example_documents, all_threads_content, example_threads, example_doc_options
from .mocks import mock_documents, mock_thread
from .validations import validate_dataset


class DatasetManagerTests(TestCase):

    def test_generate_dataset(self):
        dataset = generate_dataset(example_documents)
        validate_dataset(self, dataset, example_documents)

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
