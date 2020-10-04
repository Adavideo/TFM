from topics_identifier.models import Cluster, Document, Tree
from topics_identifier.documents_selector import short_document_types
from .example_trees import example_tree, tree_name, comments_clusters
from .mock_trees import mock_empty_tree


def mock_cluster(tree=None, num_cluster=0, level=0, with_documents=False, document_types="news"):
    if not tree:
        tree = mock_empty_tree(document_types)
    cluster_info = example_tree[level]["clusters"][num_cluster]
    cluster = Cluster(tree=tree, number=num_cluster, terms=cluster_info["terms"], level=level)
    cluster.assign_reference_document(cluster_info["reference_doc"])
    cluster.save()
    if with_documents:
        if document_types == "news":
            documents = cluster_info["documents"]
        else:
            documents = comments_clusters[num_cluster]["documents"]
        for doc in documents:
            cluster.add_document(doc)
    return cluster

def mock_clusters_list(num=3, with_documents=False):
    tree = mock_empty_tree()
    clusters_list = [ mock_cluster(tree, num_cluster=i, with_documents=with_documents) for i in range(num) ]
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
