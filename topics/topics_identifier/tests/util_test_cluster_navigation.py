from .example_datasets_and_documents import example_tree
from .util_test_clusters import validate_cluster_list, validate_number_of_children

def validate_tree_children(test, clusters_tree, level):
    parent_index = 0
    for c in clusters_tree:
        children = c["children"]
        validate_number_of_children(test, children, parent_index, level)
        parent_index += 1

def validate_clusters_tree(test, clusters_tree, level):
    clusters = []
    for c in clusters_tree:
        clusters.append(c["cluster"])
    example_clusters = example_tree[level]["clusters"]
    validate_cluster_list(test, clusters, example_clusters)
    validate_tree_children(test, clusters_tree, level)
