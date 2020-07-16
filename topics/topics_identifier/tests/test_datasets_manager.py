from django.test import TestCase
from topics_identifier.datasets_manager import *
from .example_datasets_and_documents import example_datasets, dataset_name
from .util_test_generate_clusters import create_and_store_test_clusters


class DataClassifierTests(TestCase):

    def test_load_dataset_from_file(self):
        dataset = load_dataset_from_file(dataset_name)
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
        dataset = load_dataset_from_file(dataset_name)
        store_text_dataset(dataset, dataset_name2)
        dataset2 = load_dataset_from_file(dataset_name2)
        test_dataset = example_datasets[0]
        self.assertEqual(dataset2.DESCR, test_dataset["description"])
        index = 0
        for doc in dataset.data:
            self.assertEqual(doc, test_dataset["documents"][index])
            index += 1

    def test_get_datasets_names_from_files(self):
        names = get_datasets_names_from_files()
        self.assertIs(dataset_name in names, True)

    def test_create_dataset_with_reference_documents(self):
        # Initialize
        level = 0
        create_and_store_test_clusters(level=level)
        # Execute
        dataset = create_dataset_with_reference_documents(dataset_name, level)
        # Verify
        documents = dataset.data
        example_clusters = example_datasets[0]["clusters"]
        num_clusters = len(example_clusters)
        self.assertEqual(len(documents), num_clusters)
        for index in range(0,num_clusters):
            reference_document = example_clusters[index]["reference_doc"]
            self.assertEqual(documents[index], reference_document)
