#from sklearn.datasets.base import Bunch
from .example_trees import example_tree, tree_name
from .mocks import mock_documents
from topics_identifier.models import Cluster, Document, Tree
from topics_identifier.util import short_document_types


def mock_empty_tree(document_types="both"):
    if not Document.objects.all():
        mock_documents()
    news, comments = short_document_types(document_types)
    tree = Tree(name=tree_name, news=news, comments=comments)
    tree.save()
    return tree

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

def mock_clusters_information(level):
    clusters_list = example_tree[level]["clusters"]
    terms = []
    reference_documents = []
    for cluster in clusters_list:
        terms.append(cluster["terms"])
        reference_documents.append(cluster["reference_doc"])
    clusters_information = { "terms": terms, "reference_documents": reference_documents}
    return clusters_information
