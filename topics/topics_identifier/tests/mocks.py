from sklearn.datasets.base import Bunch
from topics_identifier.models import Cluster, Document, Tree
from topics_identifier.ClustersGenerator import ClustersGenerator
from topics_identifier.TreeGenerator import TreeGenerator
from .examples import example_documents, tree_name, example_tree, example_stop_words

def mock_documents():
    for content in example_documents:
        doc = Document(content=content)
        doc.save()

def mock_empty_tree():
    tree = Tree(name=tree_name)
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

def mock_tree(max_level=0, linked=False, with_documents=True):
    tree = mock_empty_tree()
    for level in range(0, max_level+1):
        num_clusters = len(example_tree[level]["clusters"])
        for n in range(0, num_clusters):
            mock_cluster(tree, num_cluster=n, level=level, with_documents=with_documents)
        if linked:
            tree.link_children_to_parents(level)
    return tree

def mock_clusters_information(level):
    clusters_list = example_tree[level]["clusters"]
    terms = []
    reference_documents = []
    for cluster in clusters_list:
        terms.append(cluster["terms"])
        reference_documents.append(cluster["reference_doc"])
    clusters_information = { "terms": terms, "reference_documents": reference_documents}
    return clusters_information

def mock_dataset():
    dataset = Bunch()
    dataset.data = example_documents
    return dataset

def mock_cluster_generator():
    dataset = mock_dataset()
    generator = ClustersGenerator(dataset, example_stop_words)
    return generator

def mock_tree_generator(max_level):
    return TreeGenerator(tree_name, max_level)
