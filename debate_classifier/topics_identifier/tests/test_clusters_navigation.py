from django.test import TestCase
from topics_identifier.clusters_navigation import compose_clusters_list, compose_cluster_information
from .mock_clusters import mock_cluster
from .mock_trees import mock_tree
from .validations_clusters import validate_clusters_information


class ClustersNavigationTests(TestCase):

    def test_compose_cluster_information(self):
        cluster = mock_cluster()
        cluster_info = compose_cluster_information(cluster, include_documents=False)
        self.assertEqual(cluster_info["cluster"], cluster)

    def test_compose_cluster_information_with_documents(self):
        cluster = mock_cluster(with_documents=True)
        cluster_info = compose_cluster_information(cluster, include_documents=True)
        validate_clusters_information(self, cluster, cluster_info, with_children=False)

    def test_compose_cluster_information_with_children(self):
        tree = mock_tree(max_level=1, linked=True, with_documents=True)
        cluster = tree.get_cluster(cluster_number=0, level=1)
        cluster_info = compose_cluster_information(cluster, include_documents=True)
        validate_clusters_information(self, cluster, cluster_info, with_children=True)

    def test_compose_cluster_list_without_children(self):
        tree = mock_tree(max_level=0, linked=False, with_documents=True)
        clusters = tree.get_clusters_of_level(level=0)
        clusters_list = compose_clusters_list(clusters, include_documents=True)
        i = 0
        for cluster_info in clusters_list:
            validate_clusters_information(self, clusters[i], cluster_info, with_children=False)
            i += 1

    def test_compose_cluster_list_with_children(self):
        tree = mock_tree(max_level=1, linked=True, with_documents=True)
        clusters = tree.get_clusters_of_level(level=1)
        clusters_list = compose_clusters_list(clusters, include_documents=True)
        i = 0
        for cluster_info in clusters_list:
            validate_clusters_information(self, clusters[i], cluster_info, with_children=True)
            i += 1
