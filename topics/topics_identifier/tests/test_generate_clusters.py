from django.test import TestCase
from topics_identifier.generate_clusters import *
from topics_identifier.datasets_manager import generate_dataset
from topics_identifier.models import Document
from .util_test_clusters import *
from .examples import example_stop_words

class ClusteringTests(TestCase):

    def test_get_stop_words(self):
        stop_words = get_stop_words()
        self.assertEqual(stop_words, example_stop_words)

    def test_store_clusters_level0(self):
        mock_documents()
        validate_store_clusters(self, level=0)

    def test_store_clusters_level1(self):
        mock_clusters_tree(max_level=0, linked=False)
        validate_store_clusters(self, level=1)

    def test_add_documents_to_clusters(self):
        # Initialize
        level = 0
        predicted_clusters = example_tree[level]["predicted_clusters"]
        example_clusters = example_tree[level]["clusters"]
        mock_documents()
        create_and_store_test_clusters(level)
        # Execute
        add_documents_to_clusters(example_documents, predicted_clusters, tree_name, level)
        # Verify number of cllusters is correct
        created_clusters_list = Cluster.objects.filter(tree_name=tree_name)
        self.assertEqual(len(created_clusters_list), 4)
        # Verify documents are assigned to the correct cluster
        cluster_index = 0
        for cluster in created_clusters_list:
            documents = example_clusters[cluster_index]["documents"]
            validate_documents(self, cluster.documents(), documents)
            cluster_index += 1

    # Test that documents and clusters are not created twice on the database
    def test_add_documents_to_clusters_with_document_already_on_database(self):
        level = 0
        predicted_clusters = example_tree[level]["predicted_clusters"]
        example_clusters = example_tree[level]["clusters"]
        mock_documents()
        # Generate clusters and add documents twice
        for i in range(0,2):
            create_and_store_test_clusters(level=level)
            add_documents_to_clusters(example_documents, predicted_clusters, tree_name, level)
        # Verify number of cllusters is correct
        created_clusters_list = Cluster.objects.filter(tree_name=tree_name, level=level)
        self.assertEqual(len(created_clusters_list), 4)
        # Verify documents are not created or assigned twice
        cluster_index = 0
        for created_cluster in created_clusters_list:
            test_documents = example_clusters[cluster_index]["documents"]
            doc_index = 0
            cluster_documents = created_cluster.documents()
            for created_document in cluster_documents:
                # Verify the document is not created twice on the database
                doc_search = Document.objects.filter(content=created_document.content)
                self.assertIs(len(doc_search), 1)
                # Verify the document is not assigned twice to the cluster
                count = 0
                for doc in cluster_documents:
                    if doc.content == created_document.content:
                        count += 1
                self.assertIs(count, 1)
            cluster_index += 1

    def test_cluster_level0(self):
        mock_documents()
        cluster_level(tree_name, level=0)
        # Verify
        clusters = Cluster.objects.filter(tree_name=tree_name)
        example_clusters = example_tree[0]["clusters"]
        validate_cluster_list(self, clusters, example_clusters)

    def test_cluster_level1(self):
        # Initialize
        level = 1
        # mock the clusters up to the inmediate lower level
        mock_clusters_tree(level-1, linked=False)
        # Execute
        cluster_level(tree_name, level)
        # Validate
        clusters = Cluster.objects.filter(tree_name=tree_name, level=level)
        example_clusters = example_tree[level]["clusters"]
        validate_cluster_list(self, clusters, example_clusters)

    def test_link_children_clusters_to_parents_level1(self):
        level = 1
        mock_clusters_tree(level, linked=False)
        link_children_clusters_to_parents(tree_name, level)
        parents = Cluster.objects.filter(tree_name=tree_name, level=level)
        for cluster in parents:
            children = cluster.children()
            self.assertIs(len(children), 0)

    def test_link_children_clusters_to_parents_level1(self):
        level = 1
        mock_clusters_tree(level, linked=False)
        link_children_clusters_to_parents(tree_name, level)
        parents = Cluster.objects.filter(tree_name=tree_name, level=level)
        children_clusters = example_tree[level-1]["clusters"]
        example_children = [ [ children_clusters[0], children_clusters[1] ],
                             [ children_clusters[2], children_clusters[3] ]]
        i = 0
        for cluster in parents:
            children = cluster.children()
            validate_cluster_list(self, children, example_children[i])
            self.assertIs(len(children), 2)
            i += 1
