from django.test import TestCase
from topics_identifier.models import Cluster, Tree
from .examples import example_tree, example_documents_clusters
from .mocks import mock_tree, mock_documents, mock_empty_tree, mock_clusters_information
from .validations import validate_cluster, validate_clusters_list, validate_reference_documents, validate_tree_document_types


class TreeTests(TestCase):

    def test_create_tree(self):
        tree = Tree(name="", news=True, comments=True)
        validate_tree_document_types(self, tree, document_types="both")

    def test_get_cluster(self):
        # Initialize
        level = 0
        cluster_number = 0
        example_cluster = example_tree[level]["clusters"][cluster_number]
        tree = mock_tree(max_level=level, linked=False)
        # Execute
        cluster = tree.get_cluster(cluster_number, level)
        # Validate
        validate_cluster(self, cluster, example_cluster, with_documents=True)

    def test_get_clusters_of_level0(self):
        # Initialize
        level = 0
        example_clusters = example_tree[level]["clusters"]
        tree = mock_tree(max_level=level, linked=False)
        # Execute
        clusters_list = tree.get_clusters_of_level(level)
        # Validate
        validate_clusters_list(self, clusters_list, example_clusters, with_documents=True)

    def test_get_clusters_of_level1(self):
        # Initialize
        level = 1
        example_clusters = example_tree[level]["clusters"]
        tree = mock_tree(max_level=level, linked=True)
        # Execute
        clusters_list = tree.get_clusters_of_level(level)
        # Validate
        validate_clusters_list(self, clusters_list, example_clusters, with_documents=True)

    def test_get_reference_documents_level0(self):
        # Initialize
        level = 0
        example_clusters = example_tree[level]["clusters"]
        tree = mock_tree(max_level=level, linked=False)
        # Execute
        reference_documents = tree.get_reference_documents(level)
        # Validate
        validate_reference_documents(self, reference_documents, example_clusters)

    def test_get_reference_documents_level1(self):
        # Initialize
        level = 1
        example_clusters = example_tree[level]["clusters"]
        tree = mock_tree(max_level=level, linked=True)
        # Execute
        reference_documents = tree.get_reference_documents(level)
        # Validate
        validate_reference_documents(self, reference_documents, example_clusters)

    def test_add_clusters(self):
        # Initialize
        level = 0
        example_clusters = example_tree[level]["clusters"]
        mock_documents()
        tree = mock_empty_tree()
        clusters_info = mock_clusters_information(level)
        # Execute
        tree.add_clusters(level, clusters_info)
        # Validate
        clusters_list = tree.get_clusters_of_level(level)
        validate_clusters_list(self, clusters_list, example_clusters, with_documents=False)

    def test_link_children_to_parents(self):
        level = 1
        example_clusters = example_tree[level]["clusters"]
        tree = mock_tree(max_level=level, linked=False)
        tree.link_children_to_parents(parents_level=level)
        # validation
        parents = Cluster.objects.filter(tree=tree, level=level)
        validate_clusters_list(self, parents, example_clusters, with_documents=True)

    def test_add_documents_to_clusters_level0(self):
        level = 0
        example_clusters = example_tree[level]["clusters"]
        tree = mock_tree(max_level=level, linked=False, with_documents=False)
        tree.add_documents_to_clusters(level, example_documents_clusters[level])
        clusters_list = tree.get_clusters_of_level(level)
        validate_clusters_list(self, clusters_list, example_clusters, with_documents=True)

    def test_add_documents_to_clusters_level1(self):
        level = 1
        example_clusters = example_tree[level]["clusters"]
        tree = mock_tree(max_level=level, linked=True, with_documents=False)
        tree.add_documents_to_clusters(level-1, example_documents_clusters[level-1])
        tree.add_documents_to_clusters(level, example_documents_clusters[level])
        clusters_list = tree.get_clusters_of_level(level)
        validate_clusters_list(self, clusters_list, example_clusters, with_documents=True)
