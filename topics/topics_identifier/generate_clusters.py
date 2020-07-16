import datetime
from sklearn.cluster import AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets.base import Bunch
from .models import Cluster
from .file_paths import stop_words_filename
from .datasets_manager import load_dataset

def get_stop_words():
    stop_words = []
    file = open(stop_words_filename, 'r')
    words_from_file = file.read().split("\n")
    file.close()
    for word in words_from_file:
        stop_words.append(word)
    return stop_words

# Process the documents with the vectorizer.
def process_data(dataset):
    vectorizer = TfidfVectorizer(stop_words=get_stop_words())
    vectorized_documents = vectorizer.fit_transform(dataset.data)
    # Get the terms extracted from the documents (to be used later to show the results)
    terms = vectorizer.get_feature_names()
    return vectorized_documents, terms

def get_reference_document(model, cluster_number, documents):
    document_index = model.cluster_centers_indices_[cluster_number]
    reference_document = documents[document_index]
    return reference_document

def get_cluster_terms(all_terms, cluster_center):
    cluster_terms = []
    for term_index in cluster_center.indices:
        term = all_terms[term_index]
        cluster_terms.append(term)
    return cluster_terms

def update_cluster_information(cluster, cluster_center, model, terms, documents):
    cluster.terms= get_cluster_terms(terms, cluster_center)
    reference_document = get_reference_document(model, cluster.number, documents)
    cluster.assign_reference_document(content=reference_document)
    cluster.save()

def get_cluster(dataset_name, cluster_number, level):
    cluster_search = Cluster.objects.filter(dataset=dataset_name, number=cluster_number, level=level)
    if not cluster_search:
        cluster = Cluster(dataset=dataset_name, number=cluster_number, level=level)
    else:
        cluster = cluster_search[0]
    return cluster

def store_clusters(model, dataset_name, terms, documents, level):
    cluster_number = 0
    for cluster_center in model.cluster_centers_:
        cluster = get_cluster(dataset_name, cluster_number, level)
        update_cluster_information(cluster, cluster_center, model, terms, documents)
        cluster_number += 1

def add_documents_to_clusters(documents, documents_predicted_clusters, dataset_name, level=0):
    document_index = 0
    for predicted_cluster in documents_predicted_clusters:
        document = documents[document_index]
        cluster = get_cluster(dataset_name, predicted_cluster, level)
        cluster.add_document(content=document)
        document_index += 1

# Links the children clusters on the inferior level (level-1) to their parent cluster on the provided level.
# Parent clusters are the ones that include the reference document of the children cluster.
def link_children_clusters_to_parents(dataset_name, level):
    parent_clusters = Cluster.objects.filter(dataset=dataset_name, level=level)
    for parent in parent_clusters:
        children = parent.children()
        for child_cluster in children:
            child_cluster.parent = parent
            child_cluster.save()

def cluster_data(dataset, dataset_name, level):
    print(str(datetime.datetime.now().time())+" - Pre-processing documents")
    vectorized_documents, terms = process_data(dataset)
    print(str(datetime.datetime.now().time())+" - Training the model")
    model = AffinityPropagation()
    model.fit(vectorized_documents)
    print(str(datetime.datetime.now().time())+" - Predicting clusters")
    documents_predicted_clusters = model.predict(vectorized_documents)
    print(str(datetime.datetime.now().time())+" - Storing clusters information")
    store_clusters(model, dataset_name, terms, dataset.data, level)
    print(str(datetime.datetime.now().time())+" - Adding documents to clusters")
    add_documents_to_clusters(dataset.data, documents_predicted_clusters, dataset_name, level)
    print(str(datetime.datetime.now().time())+" - Linking new clusters to their children clusters in level "+str(level-1))
    link_children_clusters_to_parents(dataset_name, level)
    print(str(datetime.datetime.now().time())+" - Clustering completed")

def create_dataset_with_reference_documents(dataset_name):
    all_clusters = Cluster.objects.filter(dataset=dataset_name)
    reference_documents = []
    for cluster in all_clusters:
        reference_documents.append(cluster.reference_document.content)
    dataset = Bunch()
    dataset['data'] = reference_documents
    return dataset

def cluster_level(dataset_name, level):
    if level == 0:
        dataset = load_dataset(dataset_name)
    else:
        dataset = create_dataset_with_reference_documents(dataset_name)
    print("Generating level "+ str(level)+" clusters")
    cluster_data(dataset, dataset_name, level)
