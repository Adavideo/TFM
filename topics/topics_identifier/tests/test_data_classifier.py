from django.test import TestCase
from sklearn.cluster import KMeans, AffinityPropagation
from topics_identifier.data_classifier import cluster_data, add_documents_to_clusters, store_clusters, get_stop_words, process_data
from topics_identifier.datasets_manager import load_dataset
from topics_identifier.models import Cluster
from .examples_text_datasets_and_documents import test_dataset, cluster0, stop_words_test

class DataClassifierTests(TestCase):

    def test_cluster_data(self):
        dataset_name = test_dataset["name"]
        dataset = load_dataset(dataset_name)
        cluster_data(dataset, dataset_name)
        clusters = Cluster.objects.filter(dataset=dataset_name)
        self.assertEqual(len(clusters), 4)
        self.assertEqual(clusters[0].dataset, dataset_name)
        self.assertEqual(clusters[0].number, 0)
        self.assertEqual(clusters[0].terms, cluster0["terms"])
        self.assertEqual(clusters[0].reference_document.content, cluster0["reference_doc"])

    def test_store_clusters(self):
        # Initialize
        dataset_name = test_dataset["name"]
        documents = test_dataset["documents"]
        test_clusters = test_dataset["clusters"]
        dataset = load_dataset(dataset_name)
        vectorized_documents, terms = process_data(dataset)
        model = AffinityPropagation()
        model.fit(vectorized_documents)
        # Execute
        store_clusters(model, dataset_name, terms, documents)
        # Verify
        new_clusters = Cluster.objects.filter(dataset=dataset_name)
        self.assertEqual(len(new_clusters), 4)
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
        dataset = load_dataset(dataset_name)
        vectorized_documents, terms = process_data(dataset)
        model = AffinityPropagation()
        model.fit(vectorized_documents)
        store_clusters(model, dataset_name, terms, documents)
        # Execute
        add_documents_to_clusters(documents, test_dataset["predicted_clusters"], dataset_name)
        # Verify
        created_clusters_list = Cluster.objects.filter(dataset=dataset_name)
        self.assertEqual(len(created_clusters_list), 4)
        cluster_index = 0
        for created_cluster in created_clusters_list:
            test_cluster = test_dataset["clusters"][cluster_index]
            test_documents = test_cluster["documents"]
            doc_index = 0
            temp = []
            for created_document in created_cluster.documents():
                temp.append(created_document.content)
                self.assertEqual(created_document.content, test_documents[doc_index])
                doc_index += 1
            print(temp)
            cluster_index += 1

    def test_get_stop_words(self):
        stop_words = get_stop_words()
        self.assertEqual(stop_words, stop_words_test)
