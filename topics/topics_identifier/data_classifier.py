from sklearn.cluster import KMeans, AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer
from .input_output_files import store_clustered_documents, get_stop_words, load_dataset

def process_data(dataset):
    # Process the documents with the vectorizer.
    stop_words = get_stop_words()
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    vectorized_documents = vectorizer.fit_transform(dataset.data)
    # Get the terms extracted from the documents (to be used later to show the results)
    terms = vectorizer.get_feature_names()
    data = { "vectorized documents": vectorized_documents, "terms": terms }
    return data

def get_clusters_terms(model, terms, num_clusters):
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    clusters = []
    for i in range(num_clusters):
        cluster_terms = []
        for ind in order_centroids[i, :10]:
            cluster_terms.append(terms[ind])
        clusters.append(cluster_terms)
    return clusters

def group_documents_by_cluster(documents, documents_predicted_clusters, cluster_terms, num_clusters):
    # For each cluster stores the terms and creates an empty list to store the documents
    clustered_documents = []
    for i in range(0, num_clusters):
        clustered_documents.append({ "terms": cluster_terms[i], "documents": []})
    # Store the documents in the list of the cluster predicted
    document_index = 0
    for predicted_cluster in documents_predicted_clusters:
        document = documents[document_index]
        clustered_documents[predicted_cluster]["documents"].append(document)
        document_index += 1
    return clustered_documents

def group_documents(documents, documents_predicted_clusters, num_clusters):
    clustered_documents = []
    for i in range(0, num_clusters+1):
        clustered_documents.append({ "terms": [], "documents": []})
    # Store the documents in the list of the cluster predicted
    document_index = 0
    for predicted_cluster in documents_predicted_clusters:
        document = documents[document_index]
        clustered_documents[predicted_cluster]["documents"].append(document)
        document_index += 1
    return clustered_documents

def get_num_clusters(model):
    cluster_centers_indices = model.cluster_centers_indices_
    num_clusters = len(cluster_centers_indices)
    return num_clusters

def cluster_documents(processed_data, documents):
    model = AffinityPropagation()
    model.fit(processed_data["vectorized documents"])
    documents_predicted_clusters = model.predict(processed_data["vectorized documents"])
    num_clusters = get_num_clusters(model)
    clustered_documents = group_documents(documents, documents_predicted_clusters, num_clusters)
    #cluster_terms = get_clusters_terms(model, processed_data["terms"], num_clusters)
    #clustered_documents = group_documents_by_cluster(documents, documents_predicted_clusters, cluster_terms, num_clusters)
    return clustered_documents

def cluster_data():
    dataset = load_dataset()
    if not dataset:
        return { "clusters": [] }
    processed_data = process_data(dataset)
    clustered_documents = cluster_documents(processed_data, documents=dataset.data)
    store_clustered_documents(clustered_documents)
    return { "clusters": clustered_documents }
