from sklearn.cluster import AffinityPropagation
from topics_identifier.models import Cluster, Document
from topics_identifier.generate_clusters import store_clusters, process_data, link_children_clusters_to_parents
from topics_identifier.datasets_manager import generate_dataset
from .examples import example_tree, example_documents, tree_name


# MOCK CLUSTERS AND DOCUMENTS

def mock_cluster(num_cluster=0, level=0, documents=False):
    cluster_info = example_tree[level]["clusters"][num_cluster]
    cluster = Cluster(tree_name=tree_name, number=num_cluster, terms=cluster_info["terms"], level=level)
    cluster.assign_reference_document(cluster_info["reference_doc"])
    cluster.save()
    if documents:
        for doc in cluster_info["documents"]:
            cluster.add_document(doc)
    return cluster

def mock_clusters_with_levels(max_level, linked=False):
    for level in range(0, max_level+1):
        num_clusters = len(example_tree[level]["clusters"])
        for n in range(0, num_clusters):
            mock_cluster(num_cluster=n, level=level, documents=True)
        if linked:
            link_children_clusters_to_parents(tree_name, level)

def mock_document():
    content = example_documents[0]
    doc = Document(content=content)
    doc.save()
    return doc

def mock_documents():
    for content in example_documents:
        doc = Document(content=content)
        doc.save()


# DOCUMENTS VALIDATION

def validate_documents(test, documents, documents_info):
    test.assertEqual(len(documents), len(documents_info))
    doc_index = 0
    for doc in documents:
        test.assertEqual(doc.content, documents_info[doc_index])
        doc_index +=1

# CLUSTERS VALIDATION

def validate_cluster(test, cluster, example_cluster, documents=False):
    test.assertEqual(cluster.terms, example_cluster["terms"])
    test.assertEqual(cluster.reference_document.content, example_cluster["reference_doc"])
    if documents:
        cluster_documents = cluster.documents()
        validate_documents(test, cluster_documents, example_cluster["documents"])

def validate_cluster_list(test, cluster_list, example_clusters):
    index = 0
    for cluster in cluster_list:
        validate_cluster(test, cluster, example_clusters[index], documents=True)
        index += 1


# TREES VALIDATION

def validate_tree_children(test, clusters_tree, level):
    parent_index = 0
    for c in clusters_tree:
        children = c["children"]
        validate_number_of_children(test, children, parent_index, level)
        parent_index += 1

def validate_clusters_tree(test, clusters_tree, level):
    clusters = []
    for c in clusters_tree:
        clusters.append(c["cluster"])
    example_clusters = example_tree[level]["clusters"]
    validate_cluster_list(test, clusters, example_clusters)
    validate_tree_children(test, clusters_tree, level)


# TREES VALIDATION ON DATABASE

def validate_number_of_children(test, children, parent_index, level):
    parent_level = example_tree[level]
    num_children = parent_level["clusters"][parent_index]["num_children"]
    test.assertIs(len(children), num_children)

def validate_children(test, parent, parent_index, level):
    children = parent.children()
    validate_number_of_children(test, children, parent_index, level)
    children_level = example_tree[level-1]
    for child_index in range(0,2):
        if parent_index==0:
            example_cluster = children_level["clusters"][child_index]
        else:
            example_cluster = children_level["clusters"][child_index+2]
        validate_cluster(test, children[child_index], example_cluster)

def validate_number_of_parents(test, level, num_parents):
    # Obtain the number of clusters for this level
    num_clusters = len(example_tree[level]["clusters"])
    test.assertIs(num_parents, num_clusters)

def validate_cluster_tree(test, level):
    parents = Cluster.objects.filter(level=level)
    num_parents = len(parents)
    validate_number_of_parents(test, level, num_parents)
    for i in range(0, num_parents):
        validate_children(test, parents[i], i, level)

# VALIDATE STORE CLUSTERS

def create_and_store_test_clusters(level):
    dataset = generate_dataset(level, tree_name)
    vectorized_documents, terms = process_data(dataset)
    model = AffinityPropagation()
    model.fit(vectorized_documents)
    store_clusters(model, tree_name, terms, dataset.data, level)

def validate_store_clusters(test, level):
    example_clusters = example_tree[level]["clusters"]
    create_and_store_test_clusters(level=level)
    # Verify
    new_clusters = Cluster.objects.filter(tree_name=tree_name, level=level)
    test.assertEqual(len(new_clusters), len(example_clusters))
    index = 0
    for cluster in new_clusters:
        test.assertEqual(cluster.tree_name, tree_name)
        validate_cluster(test, cluster, example_clusters[index], documents=False)
        index += 1
