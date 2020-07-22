from django.test import TestCase
from topics_identifier.clusters_navigation import *
from .examples import example_tree, tree_name
from .util_test_clusters import *


class ClustersNavigationTests(TestCase):

    def test_get_tree_names_from_clusters(self):
        cluster = mock_cluster()
        datasets_names = get_tree_names_from_clusters()
        self.assertIs(tree_name in datasets_names, True)

    def test_get_max_level_0(self):
        mock_cluster()
        level = get_max_level(tree_name)
        self.assertIs(level, 0)

    def test_get_max_level_1(self):
        mock_clusters_with_levels(max_level=1)
        level = get_max_level(tree_name)
        self.assertIs(level, 1)

    def test_get_trees_list_empty(self):
        clusters_list = get_trees_list()
        self.assertIs(len(clusters_list), 0)

    def test_get_trees_list_with_one_cluster(self):
        mock_cluster()
        clusters_list = get_trees_list()
        self.assertIs(len(clusters_list), 1)
        self.assertEqual(clusters_list[0]["tree_name"], tree_name)
        self.assertIs(clusters_list[0]["num_clusters"], 1)
        self.assertIs(clusters_list[0]["levels"], 1)

    def test_get_trees_list_with_two_clusters(self):
        mock_cluster()
        mock_cluster(num_cluster=1)
        trees_list = get_trees_list()
        self.assertIs(len(trees_list), 1)
        self.assertIs(trees_list[0]["num_clusters"], 2)

    def test_get_trees_list_level1(self):
        mock_clusters_with_levels(max_level=1)
        datasets_list = get_trees_list()
        self.assertIs(datasets_list[0]["levels"], 2)
        self.assertIs(datasets_list[0]["num_clusters"], 4)

    # Testing the search whithout documents
    def test_get_tree(self):
        new_cluster0 = mock_cluster()
        clusters_list = get_tree(tree_name, include_documents=True)
        self.assertIs(len(clusters_list), 1)
        self.assertEqual(clusters_list[0]["cluster"], new_cluster0)
        self.assertEqual(clusters_list[0]["documents"], [])

    # Testing the search when we request the documents but there is none
    def test_get_tree_with_documents_when_no_documents_exist(self):
        new_cluster0 = mock_cluster()
        clusters_list = get_tree(tree_name, include_documents=True)
        self.assertIs(len(clusters_list), 1)
        self.assertEqual(clusters_list[0]["cluster"], new_cluster0)
        self.assertEqual(clusters_list[0]["documents"], [])

    # Testing the search with documents already assigned to one cluster
    def test_get_tree_with_documents_mock_documents_one_cluster(self):
        mock_cluster0 = mock_cluster(num_cluster=0, documents=True)
        clusters_list = get_tree(tree_name, include_documents=True)
        self.assertIs(len(clusters_list), 1)
        cluster = clusters_list[0]["cluster"]
        self.assertEqual(cluster, mock_cluster0)
        example_cluster0_documents = example_tree[0]["clusters"][0]["documents"]
        validate_documents(self, cluster.documents(), example_cluster0_documents)

    # Testing the search with documents already assigned to two cluster
    def test_get_tree_with_documents_mock_documents_two_clusters(self):
        mock_cluster0 = mock_cluster(num_cluster=0, documents=True)
        mock_cluster1 = mock_cluster(num_cluster=1, documents=True)
        clusters_list = get_tree(tree_name, include_documents=True)
        # Validate clusters
        self.assertIs(len(clusters_list), 2)
        cluster0 = clusters_list[0]["cluster"]
        self.assertEqual(cluster0, mock_cluster0)
        cluster1 = clusters_list[1]["cluster"]
        self.assertEqual(cluster1, mock_cluster1)
        # Validate documents
        cluster_index = 0
        for cluster_info in clusters_list:
            example_cluster = example_tree[0]["clusters"][cluster_index]
            example_documents = example_cluster["documents"]
            validate_documents(self, cluster_info["documents"], example_documents)
            cluster_index += 1

    # Test geting clusters for level 1 without documents
    def test_get_tree_level1(self):
        # Initialize
        level = 1
        mock_clusters_with_levels(max_level=level, linked=True)
        # Execute
        clusters_tree = get_tree(tree_name, include_documents=False)
        # Validate
        validate_clusters_tree(self, clusters_tree, level)

    # Test geting clusters for level 1 with documents
    def test_get_tree_level1_with_documents(self):
        # Initialize
        level = 1
        mock_clusters_with_levels(max_level=level, linked=True)
        # Execute
        clusters_tree = get_tree(tree_name, include_documents=True)
        # Validate
        validate_clusters_tree(self, clusters_tree, level)


    #   CLUSTERS SEARCH

    def test_get_terms_from_string_one_word(self):
        terms_string = "hola "
        terms = get_terms_from_string(terms_string)
        self.assertEqual(terms, ["hola"])

    def test_get_terms_from_string_two_words(self):
        terms_string = "hola, adios"
        terms = get_terms_from_string(terms_string)
        self.assertEqual(terms, ["hola", "adios"])

    def test_get_terms_from_string_cluster_terms_format(self):
        terms_string = "['one', 'two', 'three']"
        terms = get_terms_from_string(terms_string)
        self.assertEqual(terms, ["one", "two", "three"])

    def test_terms_match_empty_search(self):
        search_string = ""
        cluster_terms_string = "['one', 'two', 'three']"
        match = terms_match(search_string, cluster_terms_string)
        self.assertIs(match, False)

    def test_terms_match_false(self):
        search_string = "four"
        cluster_terms_string = "['one', 'two', 'three']"
        match = terms_match(search_string, cluster_terms_string)
        self.assertIs(match, False)

    def test_cluster_search_not_found(self):
        mock_clusters_with_levels(max_level=1, linked=True)
        search_string = "aaa"
        clusters_tree = cluster_search(tree_name, search_string)
        self.assertEqual(clusters_tree, [])

    def test_cluster_search_found_one_term(self):
        mock_clusters_with_levels(max_level=1, linked=True)
        search_string = "abrir"
        trees = cluster_search(tree_name, search_string)
        self.assertEqual(len(trees), 2)
        cluster0 = trees[0][0]["cluster"]
        self.assertEqual(type(cluster0), type(Cluster()))
        self.assertEqual(cluster0.level, 0)
        self.assertEqual(cluster0.number, 1)
        example_cluster0 = example_tree[0]["clusters"][1]
        validate_cluster(self, cluster0, example_cluster0, documents=False)
        cluster1 = trees[1][0]["cluster"]
        self.assertEqual(type(cluster1), type(Cluster()))
        self.assertEqual(cluster1.level, 1)
        self.assertEqual(cluster1.number, 0)
        example_cluster1 = example_tree[1]["clusters"][0]
        validate_cluster(self, cluster1, example_cluster1, documents=False)

    def test_cluster_search_found_two_terms(self):
        mock_clusters_with_levels(max_level=1, linked=True)
        search_string = "abrir, melón"
        trees = cluster_search(tree_name, search_string)
        self.assertEqual(len(trees), 2)
        cluster0 = trees[0][0]["cluster"]
        self.assertEqual(type(cluster0), type(Cluster()))
        self.assertEqual(cluster0.level, 0)
        self.assertEqual(cluster0.number, 1)
        example_cluster0 = example_tree[0]["clusters"][1]
        validate_cluster(self, cluster0, example_cluster0, documents=False)
        cluster1 = trees[1][0]["cluster"]
        self.assertEqual(type(cluster1), type(Cluster()))
        self.assertEqual(cluster1.level, 1)
        self.assertEqual(cluster1.number, 0)
        example_cluster1 = example_tree[1]["clusters"][0]
        validate_cluster(self, cluster1, example_cluster1, documents=False)
