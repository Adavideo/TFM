from django.test import TestCase
from topics_identifier.models import Cluster, Document
from .examples_text_datasets_and_documents import example_documents, test_dataset
from .util_test_clusters import mock_document, mock_cluster

class DocumentTests(TestCase):

    def test_create_document_short(self):
        doc = mock_document(type="short")
        self.assertEqual(doc.content, example_documents["short"][0])
        self.assertEqual(str(doc), "Document 1")

    def test_create_document_long(self):
        doc = mock_document(type="long")
        self.assertEqual(doc.content, example_documents["long"][0])
        self.assertEqual(str(doc), "Document 1")


class ClusterTests(TestCase):

    def test_create_cluster(self):
        cluster = mock_cluster(num_cluster=0)
        terms = test_dataset["clusters"][0]["terms"]
        self.assertEqual(cluster.dataset, test_dataset["name"])
        self.assertEqual(cluster.number, 0)
        self.assertEqual(cluster.terms, terms)

    def test_assign_reference_document(self):
        cluster = mock_cluster()
        reference_document = example_documents["short"][0]
        cluster.assign_reference_document(reference_document)
        self.assertEqual(cluster.reference_document.content, reference_document)

    def test_add_document(self):
        cluster = mock_cluster()
        doc1 = example_documents["short"][0]
        doc2 = example_documents["long"][0]
        cluster.add_document(doc1)
        cluster.add_document(doc2)
        cluster_documents = cluster.documents()
        self.assertEqual(cluster_documents[0].content, doc1)
        self.assertEqual(cluster_documents[1].content, doc2)
