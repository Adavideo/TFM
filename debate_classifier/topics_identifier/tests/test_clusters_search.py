from django.test import TestCase
from topics_identifier.models import Cluster
from topics_identifier.clusters_search import cluster_search, terms_match, get_terms_from_string
from .example_trees import example_tree
from .mock_trees import mock_tree
from .validations_clusters import validate_cluster


def validate_search_result(test, clusters_list, level, number):
    cluster = clusters_list[level]["cluster"]
    test.assertEqual(type(cluster), type(Cluster()))
    test.assertEqual(cluster.level, level)
    test.assertEqual(cluster.number, number)
    example_cluster = example_tree[level]["clusters"][number]
    validate_cluster(test, cluster, example_cluster, with_documents=False)


class ClustersSearchTests(TestCase):

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
        tree = mock_tree(max_level=1, linked=True)
        search_string = "aaa"
        clusters_tree = cluster_search(tree, search_string)
        self.assertEqual(clusters_tree, [])

    def test_cluster_search_found_one_term(self):
        tree = mock_tree(max_level=1, linked=True)
        search_string = "inmunidad"
        search_results = cluster_search(tree, search_string)
        self.assertEqual(len(search_results), 2)
        validate_search_result(self, search_results, level=0, number=2)
        validate_search_result(self, search_results, level=1, number=0)

    def test_cluster_search_found_two_terms(self):
        tree = mock_tree(max_level=1, linked=True)
        search_string = "inmunidad, coronavirus"
        search_results = cluster_search(tree, search_string)
        self.assertEqual(len(search_results), 2)
        validate_search_result(self, search_results, level=0, number=2)
        validate_search_result(self, search_results, level=1, number=0)
