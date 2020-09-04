from .validations_documents import validate_documents
from .example_trees import example_tree


# CLUSTERS VALIDATION

def validate_cluster(test, cluster, example_cluster, with_documents):
    test.assertEqual(cluster.terms, example_cluster["terms"])
    test.assertEqual(cluster.reference_document, example_cluster["reference_doc"])
    if with_documents:
        cluster_documents = cluster.documents()
        validate_documents(test, cluster_documents, example_cluster["documents"])
    # validate children
    if example_cluster["children"]:
        validate_clusters_list(test, cluster.children(), example_cluster["children"], with_documents)

def validate_clusters_list(test, clusters_list, example_clusters, with_documents):
    for i in range(len(clusters_list)):
        validate_cluster(test, clusters_list[i], example_clusters[i], with_documents)

def validate_clusters_without_tree(test, clusters_list, level):
    example_clusters = example_tree[level]["clusters"]
    for i in range(len(example_clusters)):
        cluster = clusters_list[i]
        expected = example_clusters[i]
        test.assertEqual(cluster.number, expected["num_cluster"])
        test.assertEqual(cluster.reference_document, expected["reference_doc"])
        test.assertEqual(str(cluster.terms), expected["terms"])

def validate_clusters_terms(test, clusters_terms, level):
    example_clusters = example_tree[level]["clusters"]
    for i in range(len(example_clusters)):
        test.assertEqual(str(clusters_terms[i]), example_clusters[i]["terms"])


# CLUSTERS NAVIGATION

def validate_children(test, cluster, cluster_info):
    i = 0
    for child in cluster.children():
        test.assertEqual(cluster_info["children"][i]["cluster"], child)
        i += 1

def validate_clusters_information(test, cluster, cluster_info, with_children):
    test.assertEqual(cluster_info["cluster"], cluster)
    test.assertEqual(cluster_info["documents"], cluster.documents())
    if with_children:
        validate_children(test, cluster, cluster_info)
