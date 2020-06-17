from django.test import TestCase
from topics_identifier.clustering import cluster_data, add_documents_to_clusters, get_stop_words
from topics_identifier.datasets_manager import load_dataset
from topics_identifier.models import Cluster, Document
from .examples_text_datasets_and_documents import test_dataset, stop_words_test
from .util_test_clustering import create_and_store_clusters

class ClusteringTests(TestCase):

    def test_get_stop_words(self):
        stop_words = get_stop_words()
        self.assertEqual(stop_words, stop_words_test)

    def test_store_clusters(self):
        # Initialize
        dataset_name = test_dataset["name"]
        create_and_store_clusters(test_dataset["name"], test_dataset["documents"])
        # Verify
        new_clusters = Cluster.objects.filter(dataset=dataset_name)
        self.assertEqual(len(new_clusters), 4)
        test_clusters = test_dataset["clusters"]
        index = 0
        for cluster in new_clusters:
            self.assertEqual(cluster.dataset, dataset_name)
            self.assertEqual(cluster.terms, test_clusters[index]["terms"])
            self.assertEqual(cluster.reference_document.content, test_clusters[index]["reference_doc"])
            index += 1

    def test_add_documents_to_clusters(self):
        # Initialize
        dataset_name = test_dataset["name"]
        documents = test_dataset["documents"]
        create_and_store_clusters(dataset_name, documents)
        # Execute
        add_documents_to_clusters(documents, test_dataset["predicted_clusters"], dataset_name)
        # Verify number of cllusters is correct
        created_clusters_list = Cluster.objects.filter(dataset=dataset_name)
        self.assertEqual(len(created_clusters_list), 4)
        # Verify documents are assigned to the correct cluster
        cluster_index = 0
        for created_cluster in created_clusters_list:
            test_cluster = test_dataset["clusters"][cluster_index]
            test_documents = test_cluster["documents"]
            doc_index = 0
            for created_document in created_cluster.documents():
                self.assertEqual(created_document.content, test_documents[doc_index])
                doc_index += 1
            cluster_index += 1

    # Test that documents and clusters are not created twice on the database
    def test_add_documents_to_clusters_with_document_already_on_database(self):
        # Initialize
        dataset_name = test_dataset["name"]
        documents = test_dataset["documents"]
        # Generate clusters and add documents twice
        for i in range(0,2):
            create_and_store_clusters(dataset_name, documents)
            add_documents_to_clusters(documents, test_dataset["predicted_clusters"], dataset_name)
        # Verify number of cllusters is correct
        created_clusters_list = Cluster.objects.filter(dataset=dataset_name)
        self.assertEqual(len(created_clusters_list), 4)
        # Verify documents are not created or assigned twice
        cluster_index = 0
        for created_cluster in created_clusters_list:
            test_cluster = test_dataset["clusters"][cluster_index]
            test_documents = test_cluster["documents"]
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

    def test_cluster_data(self):
        dataset_name = test_dataset["name"]
        cluster0 = test_dataset["clusters"][0]
        dataset = load_dataset(dataset_name)
        cluster_data(dataset, dataset_name)
        clusters = Cluster.objects.filter(dataset=dataset_name)
        self.assertEqual(len(clusters), 4)
        self.assertEqual(clusters[0].dataset, dataset_name)
        self.assertEqual(clusters[0].number, 0)
        self.assertEqual(clusters[0].terms, cluster0["terms"])
        self.assertEqual(clusters[0].reference_document.content, cluster0["reference_doc"])
