from topics_identifier.models import Cluster, Document
from topics_identifier.generate_clusters import link_children_clusters_to_parents
from .example_datasets_and_documents import example_datasets, example_documents, example_document_long, dataset_name

# MOCK CLUSTERS AND DOCUMENTS

def mock_cluster(num_cluster=0, level=0, documents=False):
    dataset_info = example_datasets[level]
    cluster_info = dataset_info["clusters"][num_cluster]
    cluster = Cluster(dataset=dataset_info["name"], number=num_cluster, terms=cluster_info["terms"], level=level)
    cluster.assign_reference_document(cluster_info["reference_doc"])
    cluster.save()
    if documents:
        for doc in cluster_info["documents"]:
            cluster.add_document(doc)
    return cluster

def mock_clusters_with_levels(level, linked=False):
    for l in range(0, level+1):
        example_dataset = example_datasets[l]
        num_clusters = len(example_dataset["clusters"])
        for n in range(0, num_clusters):
            mock_cluster(num_cluster=n, level=l, documents=True)
        if linked:
            link_children_clusters_to_parents(dataset_name, l)

def mock_document(type="short"):
    if type == "short":
        content = example_documents[0]
    else:
        content = example_document_long
    doc = Document(content=content)
    doc.save()
    return doc


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


# CLUSTERS TREES VALIDATION ON DATABASE

def validate_number_of_children(test, children, parent_index, level):
    parent_dataset = example_datasets[level]
    num_children = parent_dataset["clusters"][parent_index]["num_children"]
    test.assertIs(len(children), num_children)

def validate_children(test, parent, parent_index, level):
    children = parent.children()
    validate_number_of_children(test, children, parent_index, level)
    children_dataset = example_datasets[level-1]
    for child_index in range(0,2):
        if parent_index==0:
            example_cluster = children_dataset["clusters"][child_index]
        else:
            example_cluster = children_dataset["clusters"][child_index+2]
        validate_cluster(test, children[child_index], example_cluster)

def validate_number_of_parents(test, level, num_parents):
    dataset = example_datasets[level]
    # Obtain the number of clusters for this level in the example dataset
    num_clusters = len(dataset["clusters"])
    test.assertIs(num_parents, num_clusters)

def validate_cluster_tree(test, level):
    parents = Cluster.objects.filter(level=level)
    num_parents = len(parents)
    validate_number_of_parents(test, level, num_parents)
    for i in range(0, num_parents):
        validate_children(test, parents[i], i, level)