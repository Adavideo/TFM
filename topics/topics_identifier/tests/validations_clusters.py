from .validations_documents import validate_documents, validate_documents_content
from .example_trees import example_tree


# CLUSTERS VALIDATION

def validate_cluster(test, cluster, example_cluster, with_documents):
    test.assertEqual(cluster.terms, example_cluster["terms"])
    test.assertEqual(cluster.reference_document.content, example_cluster["reference_doc"])
    if with_documents:
        cluster_documents = cluster.documents()
        validate_documents(test, cluster_documents, example_cluster["documents"])
    # validate children
    if example_cluster["children"]:
        validate_clusters_list(test, cluster.children(), example_cluster["children"], with_documents)

def validate_clusters_list(test, clusters_list, example_clusters, with_documents):
    index = 0
    for cluster in clusters_list:
        validate_cluster(test, cluster, example_clusters[index], with_documents)
        index += 1

def validate_reference_documents(test, reference_documents, example_clusters):
    example_reference_documents = []
    for cluster in example_clusters:
        example_reference_documents.append(cluster["reference_doc"])
    validate_documents_content(test, reference_documents, example_reference_documents)

def validate_clusters_documents(test, clusters_documents, level):
    example_clusters = example_tree[level]["clusters"]
    for i in range(len(clusters_documents)):
        validate_documents_content(test, clusters_documents[i], example_clusters[i]["documents"])


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
