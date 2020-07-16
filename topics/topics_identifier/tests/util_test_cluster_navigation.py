from .example_datasets_and_documents import example_datasets
from .util_test_clusters import validate_cluster_list, validate_number_of_children

def validate_clusters_with_documents(test, clusters_with_documents, level, include_children):
    clusters = []
    for c in clusters_with_documents:
        clusters.append(c["cluster"])
    example_clusters = example_datasets[level]["clusters"]
    validate_cluster_list(test, clusters, example_clusters)
    if include_children:
        parent_index = 0
        for c in clusters_with_documents:
            children = c["children"]
            validate_number_of_children(test, children, parent_index, level)
            parent_index += 1
