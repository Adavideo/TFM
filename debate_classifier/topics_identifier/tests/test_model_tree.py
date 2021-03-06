from django.test import TestCase
from topics_identifier.models import Cluster, Tree
from .mocks import mock_documents
from .example_trees import example_tree, clusters_documents
from .mocks import mock_documents
from .mock_trees import mock_tree, mock_empty_tree
from .mock_clusters import mock_clusters_without_tree
from .validations import validate_documents
from .validations_clusters import validate_cluster, validate_clusters_list
from .validations_trees import validate_tree, validate_tree_documents_types


class TreeTests(TestCase):

    def test_create_tree(self):
        tree = Tree(name="", news=True, comments=True)
        validate_tree_documents_types(self, tree, documents_types="both")
        self.assertEqual(tree.max_level, 0)

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

    def test_get_max_level_clusters(self):
        # Initialize
        level = 1
        example_clusters = example_tree[level]["clusters"]
        tree = mock_tree(max_level=level, linked=True)
        # Execute
        clusters_list = tree.get_max_level_clusters()
        # Validate
        validate_clusters_list(self, clusters_list, example_clusters, with_documents=True)

    # get_clusters_of_level

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

    # get_reference_documents

    def test_get_reference_documents_level0(self):
        # Initialize
        level = 0
        tree = mock_tree(max_level=level, linked=False)
        # Execute
        reference_documents = tree.get_reference_documents(level)
        # Validate
        expected_content = example_tree[level]["reference_documents"]
        validate_documents(self, reference_documents, expected_content)

    def test_get_reference_documents_level1(self):
        # Initialize
        level = 1
        tree = mock_tree(max_level=level, linked=True)
        # Execute
        reference_documents = tree.get_reference_documents(level)
        # Validate
        expected_content = example_tree[level]["reference_documents"]
        validate_documents(self, reference_documents, expected_content)

    # add_clusters

    def test_add_clusters_level0(self):
        # Initialize
        level = 0
        mock_documents()
        tree = mock_empty_tree()
        mocked_clusters_list = mock_clusters_without_tree(level)
        # Execute
        tree.add_clusters(level, mocked_clusters_list)
        # Validate
        example_clusters = example_tree[level]["clusters"]
        clusters_list = tree.get_clusters_of_level(level)
        for i in range(len(clusters_list)):
            self.assertEqual(clusters_list[i].terms, example_clusters[i]["terms"])
        self.assertEqual(tree.max_level, level)

    def test_add_clusters_level1(self):
        # Initialize
        level = 1
        mock_documents()
        tree = mock_empty_tree()
        mocked_clusters_list = mock_clusters_without_tree(level)
        # Execute
        tree.add_clusters(level, mocked_clusters_list)
        # Validate
        example_clusters = example_tree[level]["clusters"]
        clusters_list = tree.get_clusters_of_level(level)
        for i in range(len(clusters_list)):
            self.assertEqual(clusters_list[i].terms, example_clusters[i]["terms"])
        self.assertEqual(tree.max_level, level)

    # add_documents_to_cluster

    def test_add_documents_to_cluster_level0(self):
        # Initialize
        level = 0
        example_cluster = example_tree[level]["clusters"][0]
        tree = mock_tree(max_level=level, linked=False, with_documents=False)
        documents = mock_documents(content_list=example_cluster["documents"])
        # Execute
        tree.add_documents_to_cluster(level, cluster_number=0, cluster_documents=documents)
        # Validate
        cluster = tree.get_cluster(cluster_number=0, level=level)
        validate_cluster(self, cluster, example_cluster, with_documents=True)

    def test_add_documents_to_cluster_level1(self):
        # Initialize
        level = 1
        example_cluster = example_tree[level]["clusters"][0]
        tree = mock_tree(max_level=level, linked=False, with_documents=False)
        documents = mock_documents(example_cluster["documents"])
        # Execute
        tree.add_documents_to_cluster(level, cluster_number=0, cluster_documents=documents)
        # Validate
        cluster = tree.get_cluster(cluster_number=0, level=level)
        documents = cluster.documents()
        self.assertEqual(documents[0].content, example_cluster["documents"][0])

    # link_children_to_parents

    def test_link_children_to_parents(self):
        level = 1
        example_clusters = example_tree[level]["clusters"]
        tree = mock_tree(max_level=level, linked=False)
        tree.link_children_to_parents(parents_level=level)
        # validation
        parents = Cluster.objects.filter(tree=tree, level=level)
        validate_clusters_list(self, parents, example_clusters, with_documents=True)

    def test_children_level1_clusters_not_linked(self):
        max_level = 1
        tree = mock_tree(max_level, linked=False)
        validate_tree(self, tree, max_level)

    def test_children_level1_with_linked_clusters(self):
        max_level = 1
        tree = mock_tree(max_level, linked=True)
        validate_tree(self, tree, max_level)
