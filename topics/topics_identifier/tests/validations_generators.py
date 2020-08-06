from .example_trees import example_tree

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
