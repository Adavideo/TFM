from sklearn.cluster import AffinityPropagation
from topics_identifier.datasets_manager import get_dataset
from topics_identifier.generate_clusters import store_clusters, process_data
from topics_identifier.models import Cluster
from .example_datasets_and_documents import example_datasets, dataset_name, example_documents
from .util_test_clusters import validate_cluster

def create_and_store_test_clusters(level):
    dataset = get_dataset(dataset_name, level)
    vectorized_documents, terms = process_data(dataset)
    model = AffinityPropagation()
    model.fit(vectorized_documents)
    store_clusters(model, dataset_name, terms, dataset.data, level)

def validate_store_clusters(test, level):
    example_dataset = example_datasets[level]
    example_clusters = example_dataset["clusters"]
    create_and_store_test_clusters(level=level)
    # Verify
    new_clusters = Cluster.objects.filter(dataset=dataset_name, level=level)
    test.assertEqual(len(new_clusters), len(example_clusters))
    index = 0
    for cluster in new_clusters:
        test.assertEqual(cluster.dataset, dataset_name)
        validate_cluster(test, cluster, example_clusters[index], documents=False)
        index += 1
