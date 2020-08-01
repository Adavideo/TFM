from django.test import TestCase
from topics_identifier.models import Document, Cluster
from .examples import example_documents, example_tree
from .mocks import mock_cluster, mock_tree
from .validations import validate_cluster, validate_tree

class DocumentTests(TestCase):

    def test_create_document(self):
        content = example_documents[0]
        doc = Document(content=content)
        doc.save()
        self.assertEqual(doc.content, example_documents[0])
        self.assertEqual(str(doc), "Document 1 - content: #4 Cuéntame tu,  a mi no me consta.")


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
        self.assertEqual(cluster.reference_document.content, reference_document)

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
        # Mocking cluster and checking initial state
        cluster = mock_cluster()
        all_documents = Document.objects.all()
        # When mocking the cluster, it creates the reference document
        self.assertIs(len(all_documents), 1)
        self.assertEqual(all_documents[0].content, example_documents[3])
        # Adding new document twice
        new_doc = example_documents[0]
        cluster.add_document(new_doc)
        cluster.add_document(new_doc)
        # Validating that the document is not created twice
        all_documents = Document.objects.all()
        self.assertIs(len(all_documents), 2)
        self.assertEqual(all_documents[1].content, new_doc)

    # Tets that retuns an empty array when asking for the children of level 0 clusters
    def test_children_level0(self):
        cluster = mock_cluster(level=0)
        self.assertEqual(cluster.children(), [])

    def test_children_level1_clusters_not_linked(self):
        max_level = 1
        tree = mock_tree(max_level, linked=False)
        validate_tree(self, tree, max_level)

    def test_children_level1_with_linked_clusters(self):
        max_level = 1
        tree = mock_tree(max_level, linked=True)
        validate_tree(self, tree, max_level)
