from django.test import TestCase
from topics_identifier.models import Cluster, Document, find_or_create_document
from .examples_text_datasets_and_documents import test_dataset, example_documents, create_example_document, create_example_cluster

class DocumentTests(TestCase):

    def test_create_document_short(self):
        doc = create_example_document(type="short")
        self.assertEqual(doc.content, example_documents["short"][0])
        self.assertEqual(str(doc), "Document 1")

    def test_create_document_long(self):
        doc = create_example_document(type="long")
        self.assertEqual(doc.content, example_documents["long"][0])
        self.assertEqual(str(doc), "Document 1")

    def test_find_or_create_document_created(self):
        created_doc = create_example_document(type="short")
        content = example_documents["short"][0]
        found_doc = find_or_create_document(content)
        self.assertEqual(found_doc.content, content)
        self.assertEqual(found_doc, created_doc)
        self.assertEqual(str(found_doc), str(created_doc))

    def test_find_or_create_document_not_created(self):
        content = example_documents["short"][1]
        found_doc = find_or_create_document(content)
        self.assertEqual(found_doc.content, content)
        self.assertEqual(str(found_doc), "Document 1")

class ClusterTests(TestCase):

    def test_create_cluster(self):
        cluster = create_example_cluster()
        terms = test_dataset["clusters"][0]["terms"]
        self.assertEqual(cluster.dataset, test_dataset["name"])
        self.assertEqual(cluster.number, 0)
        self.assertEqual(cluster.terms, terms)

    def test_assign_reference_document(self):
        cluster = create_example_cluster()
        reference_document = example_documents["short"][0]
        cluster.assign_reference_document(reference_document)
        self.assertEqual(cluster.reference_document.content, reference_document)

    def test_add_document(self):
        cluster = create_example_cluster()
        doc1 = example_documents["short"][0]
        doc2 = example_documents["long"][0]
        cluster.add_document(doc1)
        cluster.add_document(doc2)
        cluster_documents = cluster.documents()
        self.assertEqual(cluster_documents[0].content, doc1)
        self.assertEqual(cluster_documents[1].content, doc2)
