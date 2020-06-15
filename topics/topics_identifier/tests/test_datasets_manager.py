from django.test import TestCase
from topics_identifier.datasets_manager import load_dataset, store_text_dataset, get_datasets_names_from_files
from .examples_text_datasets_and_documents import test_dataset

class DataClassifierTests(TestCase):

    def test_load_dataset(self):
        dataset_name = test_dataset["name"]
        dataset = load_dataset(dataset_name)
        self.assertEqual(dataset.DESCR, test_dataset["description"])
        index = 0
        for doc in dataset.data:
            self.assertEqual(doc, test_dataset["documents"][index])
            index += 1
        index = 0
        for file in dataset.filenames:
            self.assertEqual(file, test_dataset["filenames"][index])
            index += 1

    def test_store_text_dataset(self):
        dataset_name = test_dataset["name"]
        dataset_name2 = "test_delete_me"
        dataset = load_dataset(dataset_name)
        store_text_dataset(dataset, dataset_name2)
        dataset2 = load_dataset(dataset_name2)
        self.assertEqual(dataset2.DESCR, test_dataset["description"])
        index = 0
        for doc in dataset.data:
            self.assertEqual(doc, test_dataset["documents"][index])
            index += 1

    def test_get_datasets_names_from_files(self):
        names = get_datasets_names_from_files()
        self.assertIs(test_dataset["name"] in names, True)
