from .validations import validate_documents
from .example_trees import example_tree


# CLUSTERS VALIDATION

def validate_cluster(test, cluster, example_cluster, with_documents, with_children=True):
    test.assertEqual(str(cluster.terms), example_cluster["terms"])
    test.assertEqual(cluster.reference_document, example_cluster["reference_doc"])
    if with_documents:
        cluster_documents = cluster.documents()
        validate_documents(test, cluster_documents, example_cluster["documents"])
    # validate children
    if example_cluster["children"] and with_children:
        children = cluster.children()
        validate_clusters_list(test, children, example_cluster["children"], with_documents)

def validate_clusters_list(test, clusters_list, expected_clusters, with_documents, with_children=True):
    num_clusters = len(expected_clusters)
    for i in range(num_clusters):
        validate_cluster(test, clusters_list[i], expected_clusters[i], with_documents, with_children)

def validate_clusters_terms(test, clusters_terms, level):
    example_clusters = example_tree[level]["clusters"]
    for i in range(len(example_clusters)):
        test.assertEqual(str(clusters_terms[i]), example_clusters[i]["terms"])

def validate_clusters_documents(test, clusters_documents, example):
    for i in range(len(example["clusters_documents"])):
        test.assertEqual(clusters_documents[i], example["clusters_documents"][i])


# CLUSTERS NAVIGATION

def validate_children(test, cluster, cluster_info):
    children = cluster.children()
    for i in range(len(children)):
        test.assertEqual(cluster_info["children"][i]["cluster"], children[i])

def validate_clusters_information(test, cluster, cluster_info, with_children):
    test.assertEqual(cluster_info["cluster"], cluster)
    test.assertEqual(cluster_info["documents"], cluster.documents())
    if with_children:
        validate_children(test, cluster, cluster_info)
