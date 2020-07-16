from django.test import TestCase
from topics_identifier.models import Cluster, Document
from .example_datasets_and_documents import example_datasets, dataset_name, example_documents, example_document_long
from .util_test_clusters import mock_document, mock_cluster, mock_clusters_with_levels, validate_cluster_tree

class DocumentTests(TestCase):

    def test_create_document_short(self):
        doc = mock_document(type="short")
        self.assertEqual(doc.content, example_documents[0])
        self.assertEqual(str(doc), "Document 1")

    def test_create_document_long(self):
        doc = mock_document(type="long")
        self.assertEqual(doc.content, example_document_long)
        self.assertEqual(str(doc), "Document 1")


class ClusterTests(TestCase):

    def test_create_cluster(self):
        cluster = mock_cluster(num_cluster=0)
        test_dataset = example_datasets[0]
        terms = test_dataset["clusters"][0]["terms"]
        self.assertEqual(cluster.dataset, dataset_name)
        self.assertEqual(cluster.number, 0)
        self.assertEqual(cluster.terms, terms)

    def test_assign_reference_document(self):
        cluster = mock_cluster()
        reference_document = example_documents[0]
        cluster.assign_reference_document(reference_document)
        self.assertEqual(cluster.reference_document.content, reference_document)

    def test_add_document(self):
        cluster = mock_cluster()
        doc1 = example_documents[0]
        doc2 = example_document_long
        cluster.add_document(doc1)
        cluster.add_document(doc2)
        cluster_documents = cluster.documents()
        self.assertEqual(cluster_documents[0].content, doc1)
        self.assertEqual(cluster_documents[1].content, doc2)

    # Tets that retuns an empty array when asking for the children of level 1 clusters
    def test_children_level0(self):
        cluster = mock_cluster(level=0)
        self.assertEqual(cluster.children(), [])

    def test_children_level1_clusters_not_linked(self):
        mock_clusters_with_levels(level=1, linked=False)
        validate_cluster_tree(self, level=1)

    def test_children_level1_with_linked_clusters(self):
        mock_clusters_with_levels(level=1, linked=True)
        validate_cluster_tree(self, level=1)
