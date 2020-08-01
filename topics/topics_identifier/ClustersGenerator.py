import datetime
from sklearn.cluster import AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer


class ClustersGenerator:

    def __init__(self, dataset, stop_words):
        self.stop_words = stop_words
        self.dataset = dataset

    # Process the documents with the vectorizer.
    def process_data(self):
        print(str(datetime.datetime.now().time())+" - Pre-processing documents")
        vectorizer = TfidfVectorizer(stop_words=self.stop_words)
        self.vectorized_documents = vectorizer.fit_transform(self.dataset.data)
        # Get the terms extracted from the documents (to be used later to show the results)
        self.terms = vectorizer.get_feature_names()

    def train_model(self):
        print(str(datetime.datetime.now().time())+" - Training the model")
        self.model = AffinityPropagation()
        self.model.fit(self.vectorized_documents)

    def get_cluster_terms(self, cluster_center):
        cluster_terms = []
        for term_index in cluster_center.indices:
            term = self.terms[term_index]
            cluster_terms.append(term)
        return cluster_terms

    def get_all_clusters_terms(self):
        all_clusters_terms = []
        for cluster_center in self.model.cluster_centers_:
            cluster_terms = self.get_cluster_terms(cluster_center)
            all_clusters_terms.append(cluster_terms)
        return all_clusters_terms

    def get_clusters_reference_documents(self):
        reference_documents_list = []
        documents = self.dataset.data
        for document_index in self.model.cluster_centers_indices_:
            reference_document = documents[document_index]
            reference_documents_list.append(reference_document)
        return reference_documents_list

    def get_clusters_information(self):
        print(str(datetime.datetime.now().time())+" - Obtaining clusters information")
        clusters_terms = self.get_all_clusters_terms()
        reference_documents = self.get_clusters_reference_documents()
        clusters_information = { "terms": clusters_terms, "reference_documents": reference_documents }
        return clusters_information

    def cluster_data(self):
        self.process_data()
        self.train_model()
        clusters_information = self.get_clusters_information()
        return clusters_information

    def get_documents_clusters(self):
        print(str(datetime.datetime.now().time())+" - Predicting documents clusters")
        predicted_clusters = self.model.predict(self.vectorized_documents)
        all_documents = self.dataset.data
        documents_clusters = []
        document_index = 0
        for cluster_number in predicted_clusters:
            doc = all_documents[document_index]
            documents_clusters.append( { "document": doc, "cluster_number": cluster_number })
            document_index += 1
        return documents_clusters
