import datetime


class ClustersGenerator:

    def __init__(self, model, vectorizer, documents):
        self.original_documents = documents
        self.model = model
        self.vectorizer = vectorizer
        self.terms = self.vectorizer.get_feature_names()
        self.number_of_clusters = self.calculate_number_of_clusters()

    def calculate_number_of_clusters(self):
        number_of_clusters = 0
        clusters_centers = self.model.cluster_centers_
        for cluster in clusters_centers:
            number_of_clusters += 1
        return number_of_clusters

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
        for document_index in self.model.cluster_centers_indices_:
            reference_document = self.original_documents[document_index]
            reference_documents_list.append(reference_document)
        return reference_documents_list

    def get_clusters_information(self):
        print(str(datetime.datetime.now().time())+" - Obtaining clusters information")
        clusters_terms = self.get_all_clusters_terms()
        reference_documents = self.get_clusters_reference_documents()
        clusters_information = { "terms": clusters_terms, "reference_documents": reference_documents }
        return clusters_information

    def get_documents_grouped_by_cluster(self, documents, predicted_clusters):
        # Create an empty array for each cluster
        documents_by_cluster = [ [] for i in range(self.number_of_clusters) ]
        # Add documents to the clusters arrays
        document_index = 0
        for cluster_number in predicted_clusters:
            doc = documents[document_index]
            documents_by_cluster[cluster_number].append(doc)
            document_index += 1
        return documents_by_cluster

    def predict_clusters_documents(self, documents):
        print(str(datetime.datetime.now().time())+" - Predicting documents clusters")
        vectorized_documents = self.vectorizer.transform(documents)
        predicted_clusters = self.model.predict(vectorized_documents)
        clusters_documents = self.get_documents_grouped_by_cluster(documents, predicted_clusters)
        return clusters_documents
