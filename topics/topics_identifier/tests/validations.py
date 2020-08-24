from sklearn.datasets.base import Bunch
from timeline.tests.validations_threads import validate_threads_list
from .validations_documents import validate_documents_content


def validate_dataset(test, dataset, expected_content):
    test.assertEqual(str(type(dataset)), "<class 'sklearn.utils.Bunch'>")
    validate_documents_content(test, dataset.data, expected_content)
