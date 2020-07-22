from sklearn.cluster import AffinityPropagation
from topics_identifier.datasets_manager import generate_dataset
from topics_identifier.generate_clusters import store_clusters, process_data
from topics_identifier.models import Cluster
from .examples import example_tree, tree_name, example_documents
from .util_test_clusters import validate_cluster, mock_documents

def create_and_store_test_clusters(level):
    dataset = generate_dataset(level, tree_name)
    vectorized_documents, terms = process_data(dataset)
    model = AffinityPropagation()
    model.fit(vectorized_documents)
    store_clusters(model, tree_name, terms, dataset.data, level)

def validate_store_clusters(test, level):
    example_clusters = example_tree[level]["clusters"]
    create_and_store_test_clusters(level=level)
    # Verify
    new_clusters = Cluster.objects.filter(tree_name=tree_name, level=level)
    test.assertEqual(len(new_clusters), len(example_clusters))
    index = 0
    for cluster in new_clusters:
        test.assertEqual(cluster.tree_name, tree_name)
        validate_cluster(test, cluster, example_clusters[index], documents=False)
        index += 1
