from topics_identifier.models import Cluster
from .examples import example_tree
from csv_import.validations import validate_documents
from csv_import.mocks import select_example_documents


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

# Compares a list of strings with the example documents
def validate_documents_content(test, documents_content, documents_info, document_types="both"):
    # Selects example documents to compare with them. They can be news, comments or both.
    selected_documents = select_example_documents(document_types, documents_info)
    test.assertEqual(len(documents_content), len(selected_documents))
    doc_index = 0
    for doc_content in documents_content:
        test.assertEqual(doc_content, selected_documents[doc_index])
        doc_index +=1

def validate_reference_documents(test, reference_documents, example_clusters):
    example_reference_documents = []
    for cluster in example_clusters:
        example_reference_documents.append(cluster["reference_doc"])
    validate_documents_content(test, reference_documents, example_reference_documents)


# TREES VALIDATION

def validate_number_of_clusters(test, level, clusters):
    # Obtain the number of clusters for this level
    num_clusters = len(example_tree[level]["clusters"])
    test.assertIs(len(clusters), num_clusters)

def validate_tree_level(test, tree, level):
    clusters_list = Cluster.objects.filter(tree=tree, level=level)
    validate_number_of_clusters(test, level, clusters_list)
    example_clusters = example_tree[level]["clusters"]
    validate_clusters_list(test, clusters_list, example_clusters, with_documents=True)

def validate_tree_document_types(test, tree, document_types):
    if document_types == "both":
        test.assertIs(tree.news, True)
        test.assertIs(tree.comments, True)
    elif document_types == "news":
        test.assertEqual(tree.news, True)
        test.assertEqual(tree.comments, False)
    else:
        test.assertEqual(tree.news, False)
        test.assertEqual(tree.comments, True)

def validate_tree(test, tree, max_level, document_types="both"):
    validate_tree_document_types(test, tree, document_types)
    for level in range(0, max_level):
        validate_tree_level(test, tree, level)


# TREE BUILDING VALIDATIONS

def validate_clusters_terms(test, all_clusters_terms, level):
    example_clusters = example_tree[level]["clusters"]
    index = 0
    for cluster_terms in all_clusters_terms:
        test.assertEqual(str(cluster_terms), example_clusters[index]["terms"])
        index += 1

def validate_clusters_reference_documents(test, clusters_reference_documents, level):
    example_clusters = example_tree[level]["clusters"]
    index = 0
    for reference_document in clusters_reference_documents:
        test.assertEqual(reference_document, example_clusters[index]["reference_doc"])
        index += 1


# NAVIGATION

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

# SEARCH

def validate_search_result(test, clusters_list, level, number):
    cluster = clusters_list[level]["cluster"]
    test.assertEqual(type(cluster), type(Cluster()))
    test.assertEqual(cluster.level, level)
    test.assertEqual(cluster.number, number)
    example_cluster = example_tree[level]["clusters"][number]
    validate_cluster(test, cluster, example_cluster, with_documents=False)
