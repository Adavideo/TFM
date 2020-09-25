from topics_identifier.models import Cluster, Document, Tree
from topics_identifier.documents_selector import short_document_types
from .example_trees import example_tree, tree_name
from .mocks import mock_documents
from .mock_trees import mock_empty_tree


def mock_cluster(tree=None, num_cluster=0, level=0, with_documents=False):
    if not tree:
        tree = mock_empty_tree()
    cluster_info = example_tree[level]["clusters"][num_cluster]
    cluster = Cluster(tree=tree, number=num_cluster, terms=cluster_info["terms"], level=level)
    cluster.assign_reference_document(cluster_info["reference_doc"])
    cluster.save()
    if with_documents:
        for doc in cluster_info["documents"]:
            cluster.add_document(doc)
    return cluster

def mock_clusters_list(num=3):
    tree = mock_empty_tree()
    clusters_list = []
    for i in range(num):
        cluster = Cluster(tree=tree, number=i, terms="", level=0)
        cluster.save()
        clusters_list.append(cluster)
    return clusters_list

def mock_clusters_without_tree(level):
    clusters_list = []
    example_clusters_info = example_tree[level]["clusters"]
    cluster_index = 0
    for cluster_info in example_clusters_info:
        cluster = Cluster(number=cluster_index, terms=cluster_info["terms"])
        clusters_list.append(cluster)
        cluster_index += 1
    return clusters_list
