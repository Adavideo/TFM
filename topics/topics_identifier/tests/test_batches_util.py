from django.test import TestCase
from topics_identifier.batches_util import *
from .examples import test_batch_size
from .examples_documents_selector import example_doc_options, doc_options_with_batches


class TreeBatchesUtilTest(TestCase):

    def test_get_batch_options_batches_true(self):
        batch_number = 1
        batch_options = get_batch_options(doc_options_with_batches, batch_number, test_batch_size)
        self.assertEqual(batch_options["size"], test_batch_size)
        self.assertEqual(batch_options["number"], batch_number)

    def test_get_batch_options_batches_false(self):
        batch_number = 1
        batch_options = get_batch_options(example_doc_options, batch_number, test_batch_size)
        self.assertEqual(batch_options, None)

    def test_get_number_of_batches_even(self):
        # Initialize
        num_documents = 10
        batch_size = 5
        # Execute
        num_batches = get_number_of_batches(num_documents, batch_size)
        # Validate
        self.assertEqual(num_batches, 2)

    def test_get_number_of_batches_uneven(self):
        # Initialize
        num_documents = 10
        batch_size = 4
        # Execute
        num_batches = get_number_of_batches(num_documents, batch_size)
        # Validate
        self.assertEqual(num_batches, 3)
