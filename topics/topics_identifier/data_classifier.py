from sklearn.cluster import KMeans, AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer
from .input_output_files import store_clusters, get_stop_words
import datetime

# Process the documents with the vectorizer.
def process_data(dataset):
    vectorizer = TfidfVectorizer(stop_words=get_stop_words())
    vectorized_documents = vectorizer.fit_transform(dataset.data)
    # Get the terms extracted from the documents (to be used later to show the results)
    terms = vectorizer.get_feature_names()
    data = { "vectorized documents": vectorized_documents, "terms": terms }
    return data

def get_cluster_terms(all_terms, terms_indices):
    cluster_terms = []
    for term_index in terms_indices:
        term = all_terms[term_index]
        cluster_terms.append(term)
    return cluster_terms

def add_cluster_documents(all_clusters_info, documents, documents_predicted_clusters):
    document_index = 0
    for predicted_cluster in documents_predicted_clusters:
        document = documents[document_index]
        all_clusters_info[predicted_cluster]["documents"].append(document)
        document_index += 1

def get_clusters_info(model, terms, documents, documents_predicted_clusters):
    all_clusters_info = []
    cluster_number = 0
    for cluster in model.cluster_centers_:
        reference_document_index = model.cluster_centers_indices_[cluster_number]
        reference_document = documents[reference_document_index]
        cluster_terms = get_cluster_terms(terms, cluster.indices)
        cluster_info = { "cluster_number": cluster_number, "terms": cluster_terms,
                            "reference_document": reference_document, "documents": [] }
        all_clusters_info.append(cluster_info)
        cluster_number += 1
    add_cluster_documents(all_clusters_info, documents, documents_predicted_clusters)
    return all_clusters_info

def cluster_documents(processed_data, documents):
    model = AffinityPropagation()
    print(str(datetime.datetime.now().time())+" - Training the model")
    model.fit(processed_data["vectorized documents"])
    print(str(datetime.datetime.now().time())+" - Predicting clusters")
    documents_predicted_clusters = model.predict(processed_data["vectorized documents"])
    print(str(datetime.datetime.now().time())+" - Reading clusters information")
    clusters_info = get_clusters_info(model, processed_data["terms"], documents, documents_predicted_clusters)
    print(str(datetime.datetime.now().time())+" - Clustering completed")
    return clusters_info

def cluster_data(dataset):
    print(str(datetime.datetime.now().time())+" - Pre-processing documents")
    processed_data = process_data(dataset)
    clusters_info = cluster_documents(processed_data, documents=dataset.data)
    store_clusters(clusters_info)
    return clusters_info
