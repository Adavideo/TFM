from django.test import TestCase
from topics_identifier.models import Document, Cluster, Tree
from .examples import example_documents, example_tree, example_date
from .mocks import mock_cluster, mock_tree, mock_documents, mock_document
from .validations import validate_cluster, validate_tree, validate_clusters_list
from csv_import.validations import validate_thread

class DocumentTests(TestCase):

    def test_create_document_news(self):
        content = example_documents[2]
        doc = mock_document(content=content, is_news=True)
        doc.save()
        self.assertEqual(doc.content, example_documents[2])
        self.assertIs(doc.is_news, True)
        self.assertEqual(str(doc), "Document 1 - type news, content: "+ example_documents[2])

    def test_create_document_comment(self):
        content = example_documents[0]
        doc = mock_document(content=content, is_news=False)
        doc.save()
        self.assertEqual(doc.content, example_documents[0])
        self.assertIs(doc.is_news, False)
        self.assertEqual(str(doc), "Document 1 - type comment, content: "+ example_documents[0])

    def test_assign_thread_comment(self):
        info = { "thread_number": 10 }
        doc = Document(content="", is_news=False, author=1, date=example_date)
        doc.assign_thread(info)
        self.assertIs(doc.thread.number, 10)

    def test_assign_thread_news(self):
        info = { "thread_number": 10, "title":"example title", "uri":"example uri" }
        doc = Document(content="", is_news=True, author=1, date=example_date)
        doc.assign_thread(info)
        validate_thread(self, doc.thread, info, is_news=True)

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
        mock_documents()
        tree = Tree(name="")
        tree.save()
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

    def test_children_level1_clusters_not_linked(self):
        max_level = 1
        tree = mock_tree(max_level, linked=False)
        validate_tree(self, tree, max_level)

    def test_children_level1_with_linked_clusters(self):
        max_level = 1
        tree = mock_tree(max_level, linked=True)
        validate_tree(self, tree, max_level)
