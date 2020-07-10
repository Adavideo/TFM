from topics_identifier.models import Cluster, Document
from topics_identifier.generate_clusters import link_children_clusters_to_parents
from .examples_text_datasets_and_documents import test_dataset_with_levels, example_documents

def mock_cluster(num_cluster=0, level=1, documents=False):
    test_dataset = test_dataset_with_levels[level-1]
    dataset_name = test_dataset["name"]
    cluster_info = test_dataset["clusters"][num_cluster]
    cluster = Cluster(dataset=dataset_name, number=num_cluster, terms=cluster_info["terms"], level=level)
    cluster.assign_reference_document(cluster_info["reference_doc"])
    cluster.save()
    if documents:
        for doc in cluster_info["documents"]:
            cluster.add_document(doc)
    return cluster

def mock_clusters_with_levels(level=2, linked=False):
    for level in range(1,level+1):
        test_dataset = test_dataset_with_levels[level-1]
        num_clusters = len(test_dataset["clusters"])
        for n in range(0, num_clusters):
            mock_cluster(num_cluster=n, level=level, documents=True)
        if linked:
            dataset_name = test_dataset_with_levels[0]["name"]
            link_children_clusters_to_parents(dataset_name, level)

def mock_document(type="short"):
    if type == "short":
        content = example_documents["short"][0]
    else:
        content = example_documents["long"][0]
    doc = Document(content=content)
    doc.save()
    return doc

def validate_cluster(test, cluster, example_cluster):
    test.assertEqual(cluster.terms, example_cluster["terms"])
    test.assertEqual(cluster.reference_document.content, example_cluster["reference_doc"])
    # Test documents
    documents = cluster.documents()
    test.assertEqual(len(documents), len(example_cluster["documents"]))
    doc_index = 0
    for doc in documents:
        test.assertEqual(doc.content, example_cluster["documents"][doc_index])
        doc_index +=1

# CHILDREN VALIDATION

def validate_number_of_children(test, children, parent_index, level):
    parent_dataset = test_dataset_with_levels[level-1]
    num_children = parent_dataset["clusters"][parent_index]["num_children"]
    test.assertIs(len(children), num_children)

def validate_children(test, parent, parent_index, level):
    children = parent.children()
    validate_number_of_children(test, children, parent_index, level)
    children_dataset = test_dataset_with_levels[level-2]
    for child_index in range(0,2):
        if parent_index==0:
            example_cluster = children_dataset["clusters"][child_index]
        else:
            example_cluster = children_dataset["clusters"][child_index+2]
        validate_cluster(test, children[child_index], example_cluster)

def validate_number_of_parents(test, level, num_parents):
    dataset = test_dataset_with_levels[level-1]
    # Obtain the number of clusters for this level in the example dataset
    num_clusters = len(dataset["clusters"])
    test.assertIs(num_parents, num_clusters)

def validate_children_level2(test):
    level = 2
    parent_clusters = Cluster.objects.filter(level=level)
    num_parents = len(parent_clusters)
    validate_number_of_parents(test, level, num_parents)
    # n = number of parent cluster
    for i in range(0, num_parents):
        parent = parent_clusters[i]
        validate_children(test, parent, i, level)
