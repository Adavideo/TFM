from topics_identifier.ClustersGenerator import ClustersGenerator
from .util_topic_annotations import *


def predict_clusters(model_name, documents):
    clusters_generator = ClustersGenerator(model_name, level=0)
    return clusters_generator.get_predicted_clusters(documents)


class RelevanceCalculator:

    def __init__(self, topic, model_name):
        self.clusters_numbers = get_topic_clusters_numbers(topic)
        self.model_name = model_name

    def cluster_belongs_to_topic(self, num_cluster):
        if num_cluster in self.clusters_numbers: return True
        else: return False

    def calculate_positives_and_negatives(self, annotated_labels, predicted_clusters):
        true_positives, false_negatives, false_positives, true_negatives = [0,0,0,0]
        num_documents = len(predicted_clusters)
        for i in range(num_documents):
            # The label according to the annotations. True: belongs to topic.
            label = annotated_labels[i]
            # True if the document has been placed by the model in a cluster that belongs to the topic.
            cluster_is_topic = self.cluster_belongs_to_topic(predicted_clusters[i])
            if label and cluster_is_topic: true_positives += 1
            if label and not cluster_is_topic: false_negatives += 1
            if not label and cluster_is_topic: false_positives += 1
            if not label and not cluster_is_topic: true_negatives += 1
        return true_positives, false_negatives, false_positives, true_negatives

    def calculate_precision_and_recall(self, values):
        true_positives, false_negatives, false_positives, true_negatives = values
        # If there is no true positives, precision and recall are both 0
        if true_positives == 0: return 0,0
        precision = true_positives / (true_positives + false_positives)
        recall = true_positives / (true_positives + false_negatives)
        return precision, recall

    def get_relevance_metrics(self, annotations):
        annotated_labels = get_labels(annotations)
        documents = get_documents_from_annotations(annotations)
        predicted_clusters = predict_clusters(self.model_name, documents)
        values = self.calculate_positives_and_negatives(annotated_labels, predicted_clusters)
        precision, recall = self.calculate_precision_and_recall(values)
        return precision, recall
