from django.test import TestCase
from topics_identifier.models import Cluster, Document
from .mocks import mock_document, mock_documents
from .mock_clusters import mock_cluster
from .mock_trees import mock_tree, mock_empty_tree
from .examples import example_documents
from .example_trees import example_tree
from .validations_clusters import validate_clusters_list, validate_cluster


class ClusterTests(TestCase):

    def test_create_cluster_without_documents(self):
        level = 0
        num_cluster = 0
        cluster = mock_cluster(num_cluster, level, with_documents=False)
        example_cluster = example_tree[level]["clusters"][num_cluster]
        validate_cluster(self, cluster, example_cluster, with_documents=False)

    def test_create_cluster_with_documents(self):
        level = 0
        num_cluster = 0
        cluster = mock_cluster(num_cluster=num_cluster, level=level, with_documents=True)
        example_cluster = example_tree[level]["clusters"][num_cluster]
        validate_cluster(self, cluster, example_cluster, with_documents=True)

    def test_assign_reference_document(self):
        cluster = mock_cluster()
        reference_document = example_documents[0]
        cluster.assign_reference_document(reference_document)
        self.assertEqual(cluster.reference_document, reference_document)

    # This test checks the functions cluster.add_document() and cluster.documents()
    def test_add_document(self):
        cluster = mock_cluster()
        documents = mock_documents(example_documents[:2])
        cluster.add_document(documents[0])
        cluster.add_document(documents[1])
        cluster_documents = cluster.documents()
        self.assertEqual(cluster_documents, documents)

    # Ensure that the same document is not stored twice
    def test_add_document_twice(self):
        mock_document()
        tree = mock_empty_tree()
        cluster = Cluster(tree=tree, level=0, number=0)
        cluster.save()
        # Adding new document twice
        document = mock_document(example_documents[0])
        cluster.add_document(document)
        cluster.add_document(document)
        # Validating that the document is not created twice
        documents = cluster.documents()
        self.assertIs(len(documents), 1)
        self.assertEqual(documents[0], document)

    def test_find_children_by_reference_document(self):
        level = 1
        cluster_number = 0
        tree = mock_tree(level, linked=False)
        cluster = tree.get_cluster(cluster_number, level)
        children = cluster.find_children_by_reference_document()
        example_cluster = example_tree[level]["clusters"][cluster_number]
        validate_clusters_list(self, children, example_cluster["children"], with_documents=True)

    # Tets that retuns an empty array when asking for the children of level 0 clusters
    def test_children_level0(self):
        cluster = mock_cluster(level=0)
        self.assertEqual(cluster.children(), [])
