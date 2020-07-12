from django.test import TestCase
from topics_identifier.datasets_manager import load_dataset, store_text_dataset, get_datasets_names_from_files
from .example_datasets_and_documents import example_datasets, dataset_name

class DataClassifierTests(TestCase):

    def test_load_dataset(self):
        dataset = load_dataset(dataset_name)
        test_dataset = example_datasets[0]
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
        dataset_name2 = "test_delete_me"
        dataset = load_dataset(dataset_name)
        store_text_dataset(dataset, dataset_name2)
        dataset2 = load_dataset(dataset_name2)
        test_dataset = example_datasets[0]
        self.assertEqual(dataset2.DESCR, test_dataset["description"])
        index = 0
        for doc in dataset.data:
            self.assertEqual(doc, test_dataset["documents"][index])
            index += 1

    def test_get_datasets_names_from_files(self):
        names = get_datasets_names_from_files()
        self.assertIs(dataset_name in names, True)
