from .data_importer import load_dataset
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd

def process_data(dataset):
    # Process the documents with the vectorizer.
    vectorizer = TfidfVectorizer()
    vectorized_documents = vectorizer.fit_transform(dataset.data)
    # Get the terms extracted from the documents (to be used later to show the results)
    terms = vectorizer.get_feature_names()
    data = { "vectorized documents": vectorized_documents, "terms": terms }
    return data

def get_clusters(model, terms, num_clusters):
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    clusters = []
    for i in range(num_clusters):
        cluster_terms = []
        for ind in order_centroids[i, :10]:
            cluster_terms.append(terms[ind])
        clusters.append(cluster_terms)
    return clusters

def cluster_with_kmeans(data):
    num_clusters = 40
    # Build the model
    model = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=100, n_init=1)
    # Train the model with the pre procesed data
    model.fit(data["vectorized documents"])
    # Read the results: clusters and the terms selected for each of them
    clusters = get_clusters(model, data["terms"], num_clusters)
    return clusters

def cluster_data():
    # Load the dataset with text documents
    dataset = load_dataset()
    processed_data = process_data(dataset)
    clusters = cluster_with_kmeans(processed_data)
    return { "documents": dataset.data, "clusters":clusters }
