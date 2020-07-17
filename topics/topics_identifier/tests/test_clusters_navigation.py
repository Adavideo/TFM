from django.test import TestCase
from topics_identifier.clusters_navigation import *
from .example_datasets_and_documents import example_datasets, dataset_name
from .util_test_clusters import mock_cluster, validate_documents, mock_clusters_with_levels, validate_cluster_list
from .util_test_cluster_navigation import *

class ClustersNavigationTests(TestCase):

    def test_get_datasets_names_from_clusters(self):
        cluster = mock_cluster()
        datasets_names = get_datasets_names_from_clusters()
        self.assertIs(dataset_name in datasets_names, True)

    def test_get_max_level_0(self):
        mock_cluster()
        level = get_max_level(dataset_name)
        self.assertIs(level, 0)

    def test_get_max_level_1(self):
        mock_clusters_with_levels(level=1)
        level = get_max_level(dataset_name)
        self.assertIs(level, 1)

    def test_get_datasets_clusters_list_empty(self):
        clusters_list = get_datasets_clusters_list()
        self.assertIs(len(clusters_list), 0)

    def test_get_datasets_clusters_list_with_one_cluster(self):
        mock_cluster()
        datasets_list = get_datasets_clusters_list()
        self.assertIs(len(datasets_list), 1)
        self.assertEqual(datasets_list[0]["dataset_name"], dataset_name)
        self.assertIs(datasets_list[0]["num_clusters"], 1)
        self.assertIs(datasets_list[0]["levels"], 1)

    def test_get_datasets_clusters_list_with_two_clusters(self):
        mock_cluster()
        mock_cluster(num_cluster=1)
        datasets_list = get_datasets_clusters_list()
        self.assertIs(len(datasets_list), 1)
        self.assertIs(datasets_list[0]["num_clusters"], 2)

    def test_get_datasets_clusters_list_level1(self):
        mock_clusters_with_levels(level=1)
        datasets_list = get_datasets_clusters_list()
        self.assertIs(datasets_list[0]["levels"], 2)
        self.assertIs(datasets_list[0]["num_clusters"], 4)

    # Testing the search without indicating the name of the dataset
    def test_get_clusters_with_documents_no_data_name_no_documents(self):
        new_cluster0 = mock_cluster()
        clusters_list = get_clusters_with_documents()
        self.assertIs(len(clusters_list), 1)
        self.assertEqual(clusters_list[0]["cluster"], new_cluster0)
        self.assertEqual(clusters_list[0]["documents"], [])

    # Testing the search indicating the name of the dataset
    def test_get_clusters_with_documents_search_data_name_no_documents(self):
        new_cluster0 = mock_cluster()
        clusters_list = get_clusters_with_documents(dataset_name)
        self.assertIs(len(clusters_list), 1)
        self.assertEqual(clusters_list[0]["cluster"], new_cluster0)
        self.assertEqual(clusters_list[0]["documents"], [])

    # Testing the search with documents already assigned to one cluster
    def test_get_clusters_with_documents_mock_documents_one_cluster(self):
        mock_cluster0 = mock_cluster(num_cluster=0, documents=True)
        clusters_list = get_clusters_with_documents(dataset_name)
        self.assertIs(len(clusters_list), 1)
        cluster = clusters_list[0]["cluster"]
        self.assertEqual(cluster, mock_cluster0)
        example_cluster0_documents = example_datasets[0]["clusters"][0]["documents"]
        validate_documents(self, cluster.documents(), example_cluster0_documents)

    # Testing the search with documents already assigned to two cluster
    def test_get_clusters_with_documents_mock_documents_two_clusters(self):
        mock_cluster0 = mock_cluster(num_cluster=0, documents=True)
        mock_cluster1 = mock_cluster(num_cluster=1, documents=True)
        clusters_list = get_clusters_with_documents(dataset_name)
        # Validate clusters
        self.assertIs(len(clusters_list), 2)
        cluster0 = clusters_list[0]["cluster"]
        self.assertEqual(cluster0, mock_cluster0)
        cluster1 = clusters_list[1]["cluster"]
        self.assertEqual(cluster1, mock_cluster1)
        # Validate documents
        cluster_index = 0
        for cluster_info in clusters_list:
            example_cluster = example_datasets[0]["clusters"][cluster_index]
            example_documents = example_cluster["documents"]
            validate_documents(self, cluster_info["documents"], example_documents)
            cluster_index += 1

    # Test geting clusters for level 1
    def test_get_clusters_level1(self):
        # Initialize
        level = 1
        mock_clusters_with_levels(level, linked=False)
        # Execute
        clusters_with_documents = get_clusters_with_documents(dataset_name, level)
        # Validate
        validate_clusters_with_documents(self, clusters_with_documents, level, include_children=False)

    def test_get_clusters_level1_with_children(self):
        # Initialize
        level = 1
        mock_clusters_with_levels(level, linked=True)
        # Execute
        clusters_with_documents = get_clusters_with_documents(dataset_name, level, include_children=True)
        # Validate
        validate_clusters_with_documents(self, clusters_with_documents, level, include_children=True)
