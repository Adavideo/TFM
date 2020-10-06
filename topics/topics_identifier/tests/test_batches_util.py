from django.test import TestCase
from topics_identifier.batches_util import get_number_of_batches, get_batch_limits
from .examples import test_batch_size
from .mocks import mock_documents


class TreeBatchesUtilTest(TestCase):

    # get_number_of_batches

    def test_get_number_of_batches_even(self):
        num_batches = get_number_of_batches(num_documents = 10, size = 5)
        self.assertEqual(num_batches, 2)

    def test_get_number_of_batches_uneven(self):
        num_batches = get_number_of_batches(num_documents = 10, size = 4)
        self.assertEqual(num_batches, 3)

    # get_batch_limits

    def test_select_documents_batch_1(self):
        #Initialize
        mock_documents()
        #Execute
        start, end = get_batch_limits(batch_number=1, size=test_batch_size)
        #Validate
        self.assertEqual(start, 0)
        self.assertEqual(end, test_batch_size)

    def test_get_documents_batch_2(self):
        #Initialize
        mock_documents()
        #Execute
        start, end = get_batch_limits(batch_number=2, size=test_batch_size)
        #Validate
        self.assertEqual(start, test_batch_size)
        self.assertEqual(end, test_batch_size*2)
