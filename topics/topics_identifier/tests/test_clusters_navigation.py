from django.test import TestCase
from topics_identifier.clusters_navigation import get_datasets_names_from_clusters, get_datasets_clusters_list, get_clusters_with_documents
from .examples_text_datasets_and_documents import test_dataset, create_example_cluster

class ClustersNavigationTests(TestCase):

    def test_get_datasets_names_from_clusters(self):
        cluster = create_example_cluster()
        datasets_names = get_datasets_names_from_clusters()
        self.assertIs(test_dataset["name"] in datasets_names, True)

    def test_get_datasets_clusters_list_empty(self):
        clusters_list = get_datasets_clusters_list()
        self.assertIs(len(clusters_list), 0)

    def test_get_datasets_clusters_list_with_one_cluster(self):
        create_example_cluster()
        datasets_list = get_datasets_clusters_list()
        self.assertIs(len(datasets_list), 1)
        self.assertEqual(datasets_list[0]["dataset_name"], test_dataset["name"])
        self.assertIs(datasets_list[0]["num_clusters"], 1)

    def test_get_datasets_clusters_list_with_two_clusters(self):
        create_example_cluster()
        create_example_cluster(number=1)
        datasets_list = get_datasets_clusters_list()
        self.assertIs(len(datasets_list), 1)
        self.assertIs(datasets_list[0]["num_clusters"], 2)

    # Testing the search without indicating the name of the dataset
    def test_get_clusters_with_documents_no_data_name_no_documents(self):
        new_cluster0 = create_example_cluster()
        clusters_list = get_clusters_with_documents()
        self.assertIs(len(clusters_list), 1)
        self.assertEqual(clusters_list[0]["cluster"], new_cluster0)
        self.assertEqual(clusters_list[0]["documents"], [])

    # Testing the search indicating the name of the dataset
    def test_get_clusters_with_documents_search_data_name_no_documents(self):
        new_cluster0 = create_example_cluster()
        clusters_list = get_clusters_with_documents(dataset_name=test_dataset["name"])
        self.assertIs(len(clusters_list), 1)
        self.assertEqual(clusters_list[0]["cluster"], new_cluster0)
        self.assertEqual(clusters_list[0]["documents"], [])

    # Testing the search with documents already assigned to one cluster
    def test_get_clusters_with_documents_mock_documents_one_cluster(self):
        new_cluster0 = create_example_cluster(number=0, documents=True)
        clusters_list = get_clusters_with_documents(dataset_name=test_dataset["name"])
        self.assertIs(len(clusters_list), 1)
        self.assertEqual(clusters_list[0]["cluster"], new_cluster0)
        doc_index = 0
        for doc in clusters_list[0]["documents"]:
            test_documents = test_dataset["clusters"][0]["documents"]
            self.assertEqual(doc.content, test_documents[doc_index])
            doc_index += 1

    # Testing the search with documents already assigned to two cluster
    def test_get_clusters_with_documents_mock_documents_two_clusters(self):
        new_cluster0 = create_example_cluster(number=0, documents=True)
        new_cluster1 = create_example_cluster(number=1, documents=True)
        clusters_list = get_clusters_with_documents(dataset_name=test_dataset["name"])
        self.assertIs(len(clusters_list), 2)
        self.assertEqual(clusters_list[0]["cluster"], new_cluster0)
        self.assertEqual(clusters_list[1]["cluster"], new_cluster1)
        cluster_index = 0
        for cluster_info in clusters_list:
            doc_index = 0
            test_cluster = test_dataset["clusters"][cluster_index]
            for doc in cluster_info["documents"]:
                test_documents = test_cluster["documents"]
                self.assertEqual(doc.content, test_documents[doc_index])
                doc_index += 1
            cluster_index += 1
