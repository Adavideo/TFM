from sklearn.cluster import KMeans, AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer
from .input_output_files import get_stop_words
from .models import Cluster
import datetime

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

def get_cluster(dataset_name, cluster_number):
    cluster_search = Cluster.objects.filter(dataset=dataset_name, number=cluster_number)
    if not cluster_search:
        cluster = Cluster(dataset=dataset_name, number=cluster_number)
    else:
        cluster = cluster_search[0]
    return cluster

def store_clusters(model, dataset_name, terms, documents):
    cluster_number = 0
    for cluster_center in model.cluster_centers_:
        cluster = get_cluster(dataset_name, cluster_number)
        update_cluster_information(cluster, cluster_center, model, terms, documents)
        cluster_number += 1

def add_documents_to_clusters(documents, documents_predicted_clusters, dataset_name):
    document_index = 0
    for predicted_cluster in documents_predicted_clusters:
        document = documents[document_index]
        cluster = get_cluster(dataset_name, predicted_cluster)
        cluster.add_document(content=document)
        document_index += 1

def cluster_data(dataset, dataset_name):
    print(str(datetime.datetime.now().time())+" - Pre-processing documents")
    vectorized_documents, terms = process_data(dataset)
    print(str(datetime.datetime.now().time())+" - Training the model")
    model = AffinityPropagation()
    model.fit(vectorized_documents)
    print(str(datetime.datetime.now().time())+" - Predicting clusters")
    documents_predicted_clusters = model.predict(vectorized_documents)
    print(str(datetime.datetime.now().time())+" - Storing clusters information")
    store_clusters(model, dataset_name, terms, dataset.data)
    print(str(datetime.datetime.now().time())+" - Adding documents to clusters")
    add_documents_to_clusters(dataset.data, documents_predicted_clusters, dataset_name)
    print(str(datetime.datetime.now().time())+" - Clustering completed")
