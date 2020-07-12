from django.test import TestCase
from topics_identifier.generate_clusters import cluster_data, add_documents_to_clusters, get_stop_words, create_dataset_with_reference_documents, cluster_level
from topics_identifier.datasets_manager import load_dataset
from topics_identifier.models import Cluster, Document
from .example_datasets_and_documents import example_datasets, dataset_name, example_documents
from .util_test_generate_clusters import create_and_store_test_clusters
from .util_test_clusters import validate_cluster, validate_documents, validate_cluster_list
from .example_stop_words import example_stop_words

class ClusteringTests(TestCase):

    def test_get_stop_words(self):
        stop_words = get_stop_words()
        self.assertEqual(stop_words, example_stop_words)

    def test_store_clusters_level1(self):
        # Initialize
        example_dataset = example_datasets[0]
        example_clusters = example_dataset["clusters"]
        create_and_store_test_clusters(dataset_name, example_documents)
        # Verify
        new_clusters = Cluster.objects.filter(dataset=dataset_name)
        self.assertEqual(len(new_clusters), 4)
        index = 0
        for cluster in new_clusters:
            self.assertEqual(cluster.dataset, dataset_name)
            validate_cluster(self, cluster, example_clusters[index], documents=False)
            index += 1

    def test_add_documents_to_clusters(self):
        # Initialize
        example_dataset = example_datasets[0]
        create_and_store_test_clusters(dataset_name, example_documents)
        # Execute
        add_documents_to_clusters(example_documents, example_dataset["predicted_clusters"], dataset_name)
        # Verify number of cllusters is correct
        created_clusters_list = Cluster.objects.filter(dataset=dataset_name)
        self.assertEqual(len(created_clusters_list), 4)
        # Verify documents are assigned to the correct cluster
        cluster_index = 0
        for created_cluster in created_clusters_list:
            example_cluster = example_dataset["clusters"][cluster_index]
            validate_documents(self, created_cluster.documents(), example_cluster["documents"])
            cluster_index += 1

    # Test that documents and clusters are not created twice on the database
    def test_add_documents_to_clusters_with_document_already_on_database(self):
        test_dataset = example_datasets[0]
        # Generate clusters and add documents twice
        for i in range(0,2):
            create_and_store_test_clusters(dataset_name, example_documents)
            add_documents_to_clusters(example_documents, test_dataset["predicted_clusters"], dataset_name)
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

    def test_cluster_data_level1(self):
        # Initialize
        dataset = load_dataset(dataset_name)
        # Execute
        cluster_data(dataset, dataset_name)
        # Verify
        clusters = Cluster.objects.filter(dataset=dataset_name)
        example_clusters = example_datasets[0]["clusters"]
        validate_cluster_list(self, clusters, example_clusters)

    def test_create_dataset_with_reference_documents(self):
        # Initialize
        create_and_store_test_clusters(dataset_name, example_documents)
        # Execute
        dataset_level2 = create_dataset_with_reference_documents(dataset_name)
        # Verify
        documents = dataset_level2.data
        example_clusters = example_datasets[0]["clusters"]
        num_clusters = len(example_clusters)
        self.assertEqual(len(documents), num_clusters)
        for index in range(0,num_clusters):
            reference_document = example_clusters[index]["reference_doc"]
            self.assertEqual(documents[index], reference_document)

    def test_cluster_data_level2(self):
        # Initialize
        create_and_store_test_clusters(dataset_name, example_documents)
        # Execute
        cluster_level(dataset_name, level=2)
        # Validate
        clusters = Cluster.objects.filter(dataset=dataset_name, level=2)
        self.assertEqual(len(clusters), 2)
        example_clusters_level2 = example_datasets[1]["clusters"]
        validate_cluster_list(self, clusters, example_clusters_level2)
