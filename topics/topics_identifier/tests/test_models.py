from django.test import TestCase
from topics_identifier.models import Cluster, Document, find_or_create_document
from .examples_documents import *

class DocumentTests(TestCase):

    def test_create_document_short(self):
        content = example_documents_short[0]
        doc = Document(content=content)
        doc.save()
        self.assertEqual(doc.content, content)
        self.assertEqual(str(doc), "Document 1")

    def test_create_document_long(self):
        content = example_documents_long[0]
        doc = Document(content=content)
        doc.save()
        self.assertEqual(doc.content, content)
        self.assertEqual(str(doc), "Document 1")

    def test_find_or_create_document_created(self):
        content = example_documents_short[1]
        created_doc = Document(content=content)
        created_doc.save()
        found_doc = find_or_create_document(content)
        self.assertEqual(found_doc.content, content)
        self.assertEqual(found_doc, created_doc)
        self.assertEqual(str(found_doc), str(created_doc))

    def test_find_or_create_document_not_created(self):
        content = example_documents_short[2]
        found_doc = find_or_create_document(content)
        self.assertEqual(found_doc.content, content)
        self.assertEqual(str(found_doc), "Document 1")

class ClusterTests(TestCase):

    def test_create_cluster(self):
        dataset_name = "Test dataset"
        terms = str(example_terms1)
        cluster = Cluster(dataset=dataset_name, number=0, terms=terms)
        cluster.save()
        self.assertEqual(cluster.dataset, dataset_name)
        self.assertEqual(cluster.number, 0)
        self.assertEqual(cluster.terms, terms)

    def test_assign_reference_document(self):
        dataset_name = "Test dataset"
        terms = str(example_terms1)
        cluster = Cluster(dataset=dataset_name, number=0, terms=terms)
        cluster.save()
        reference_document = example_documents_short[0]
        cluster.assign_reference_document(reference_document)
        self.assertEqual(cluster.reference_document.content, reference_document)

    def test_add_document(self):
        dataset_name = "Test dataset"
        terms = str(example_terms1)
        cluster = Cluster(dataset=dataset_name, number=0, terms=terms)
        cluster.save()
        doc1 = example_documents_short[0]
        doc2 = example_documents_long[0]
        cluster.add_document(doc1)
        cluster.add_document(doc2)
        cluster_documents = cluster.documents()
        self.assertEqual(cluster_documents[0].content, doc1)
        self.assertEqual(cluster_documents[1].content, doc2)
