from .example_trees import example_tree
from .validations import validate_documents
from .validations_clusters import validate_clusters_list


def validate_tree_documents_types(test, tree, documents_types):
    if documents_types == "both":
        test.assertIs(tree.news, True)
        test.assertIs(tree.comments, True)
    elif documents_types == "news":
        test.assertEqual(tree.news, True)
        test.assertEqual(tree.comments, False)
    else:
        test.assertEqual(tree.news, False)
        test.assertEqual(tree.comments, True)

def validate_number_of_clusters(test, level, clusters):
    # Obtain the number of clusters for this level
    num_clusters = len(example_tree[level]["clusters"])
    test.assertIs(len(clusters), num_clusters)

def validate_tree_level(test, tree, level, with_documents=True, with_children=True):
    clusters_list = tree.get_clusters_of_level(level)
    validate_number_of_clusters(test, level, clusters_list)
    example_clusters = example_tree[level]["clusters"]
    validate_clusters_list(test, clusters_list, example_clusters, with_documents, with_children)

def validate_tree(test, tree, max_level, documents_types="both"):
    validate_tree_documents_types(test, tree, documents_types)
    for level in range(0, max_level):
        validate_tree_level(test, tree, level)

def validate_level_clusters_documents(test, tree, level):
    clusters_list = tree.get_clusters_of_level(level)
    example_clusters = example_tree[level]["clusters"]
    for i in range(len(clusters_list)):
        cluster_documents = clusters_list[i].documents()
        validate_documents(test, cluster_documents, example_clusters[i]["documents"])
