from django.test import TestCase
from .mock_clusters import mock_cluster
from .mock_trees import mock_tree, mock_empty_tree
from .mock_documents import mock_document
from .example_trees import example_tree
from .example_documents import example_documents
from .validations_clusters import validate_clusters_list, validate_cluster
from topics_identifier.models import Tree, Cluster, Document

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
        cluster = mock_cluster(num_cluster, level, with_documents=True)
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
        doc1 = example_documents[0]
        doc2 = example_documents[1]
        cluster.add_document(doc1)
        cluster.add_document(doc2)
        cluster_documents = cluster.documents()
        self.assertEqual(cluster_documents[0].content, doc1)
        self.assertEqual(cluster_documents[1].content, doc2)

    # Ensure that the same document is not stored twice
    def test_add_document_twice(self):
        mock_document()
        tree = mock_empty_tree()
        cluster = Cluster(tree=tree, level=0, number=0)
        cluster.save()
        # Adding new document twice
        content = example_documents[0]
        cluster.add_document(content)
        cluster.add_document(content)
        # Validating that the document is not created twice
        documents = Document.objects.filter(content=content)
        self.assertIs(len(documents), 1)
        self.assertEqual(documents[0].content, content)

    def test_find_children_by_reference_document(self):
        level = 1
        cluster_number = 0
        tree = mock_tree(level, linked=False)
        cluster = tree.get_cluster(cluster_number, level)
        children = cluster.find_children_by_reference_document()
        self.assertEqual(len(children), 2)
        example_clusters = example_tree[level]["clusters"][cluster_number]["children"]
        validate_clusters_list(self, children, example_clusters, with_documents=True)

    # Tets that retuns an empty array when asking for the children of level 0 clusters
    def test_children_level0(self):
        cluster = mock_cluster(level=0)
        self.assertEqual(cluster.children(), [])
