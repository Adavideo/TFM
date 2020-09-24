import datetime
from .models import Cluster, Document
from .errors import loading_files_errors


class ClustersGenerator:

    def __init__(self, models_manager, level, model=None, vectorizer=None):
        self.level = level
        self.models_manager = models_manager
        self.load_model_and_vectorizer(model, vectorizer)
        self.load_clusters_information()

    def load_model_and_vectorizer(self, model, vectorizer):
        print(str(datetime.datetime.now().time())+" - Loading model "+self.models_manager.name)
        if not model:
            model = self.models_manager.load_object("model", self.level)
        if not vectorizer:
            vectorizer = self.models_manager.load_object("vectorizer", self.level)
        self.model = model
        self.vectorizer = vectorizer

    def load_clusters_information(self):
        try:
            self.number_of_clusters = self.calculate_number_of_clusters()
            self.terms = self.vectorizer.get_feature_names()
            self.reference_documents = self.models_manager.load_object("reference_documents", self.level)
        except:
            error = loading_files_errors(self.model, self.vectorizer, self.level)
            return error

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

    def get_clusters(self):
        print(str(datetime.datetime.now().time())+" - Obtaining clusters")
        try:
            clusters_terms = self.get_all_clusters_terms()
            clusters_list = []
            for cluster_index in range(self.number_of_clusters):
                cluster = Cluster(number=cluster_index)
                cluster.terms = clusters_terms[cluster_index]
                reference_document = self.reference_documents[cluster_index]
                cluster.assign_reference_document(reference_document)
                clusters_list.append(cluster)
            return clusters_list
        except:
            error = loading_files_errors(self.model, self.vectorizer, self.level)
            return error

    def get_reference_documents(self, original_documents):
        self.reference_documents = []
        for document_index in self.model.cluster_centers_indices_:
            content = original_documents[document_index]
            self.reference_documents.append(content)
        return self.reference_documents

    def get_documents_grouped_by_cluster(self, documents, predicted_clusters):
        print(str(datetime.datetime.now().time())+" - Ordering documents according to the predicted clusters")
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
