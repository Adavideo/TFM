from django.test import TestCase
from common.testing.example_models import test_model_name
from .examples_annotations import annotations_examples
from .mock_annotations import mock_topic_annotations, mock_topic_cluster, mock_topic
from metrics.RelevanceCalculator import RelevanceCalculator, get_labels


class RelevanceCalculatorTests(TestCase):

    def test_create_relevance_calculator(self):
        topic, annotations = mock_topic_annotations(annotations_examples["agreement"])
        relevance_calculator = RelevanceCalculator(topic, test_model_name)

    def test_get_labels_agreement(self):
        topic, annotations = mock_topic_annotations(annotations_examples["agreement"])
        labels = get_labels(annotations)
        self.assertEqual(labels, [True, False, False, True])

    def test_get_labels_small_disagreement(self):
        topic, annotations = mock_topic_annotations(annotations_examples["small disagreement"])
        labels = get_labels(annotations)
        self.assertEqual(labels, [True, False, False, True])

    def test_calculate_positives_and_negatives_two_false_negatives_two_true_negatives(self):
        topic = mock_topic()
        annotated_labels = [True, False, False, True]
        predicted_clusters = [0, 0, 1, 1]
        relevance_calculator = RelevanceCalculator(topic, test_model_name)
        values = relevance_calculator.calculate_positives_and_negatives(annotated_labels, predicted_clusters)
        # true_positives, false_negatives, false_positives, true_negatives
        self.assertEqual(values, (0,2,0,2))

    def test_calculate_positives_and_negatives_all_true_negatives(self):
        topic = mock_topic()
        annotated_labels = [False, False, False, False]
        predicted_clusters = [0, 0, 1, 1]
        relevance_calculator = RelevanceCalculator(topic, test_model_name)
        values = relevance_calculator.calculate_positives_and_negatives(annotated_labels, predicted_clusters)
        # true_positives, false_negatives, false_positives, true_negatives
        self.assertEqual(values, (0,0,0,4))

    def test_calculate_positives_and_negatives_one_of_each(self):
        topic = mock_topic()
        mock_topic_cluster(topic, num_cluster=0)
        annotated_labels = [True, False, False, True]
        predicted_clusters = [0, 0, 1, 1]
        relevance_calculator = RelevanceCalculator(topic, test_model_name)
        values = relevance_calculator.calculate_positives_and_negatives(annotated_labels, predicted_clusters)
        # true_positives, false_negatives, false_positives, true_negatives
        self.assertEqual(values, (1,1,1,1))

    def test_calculate_positives_and_negatives_two_false_positives_two_true_negatives(self):
        topic = mock_topic()
        mock_topic_cluster(topic, num_cluster=0)
        annotated_labels = [False, False, False, False]
        predicted_clusters = [0, 0, 1, 1]
        relevance_calculator = RelevanceCalculator(topic, test_model_name)
        values = relevance_calculator.calculate_positives_and_negatives(annotated_labels, predicted_clusters)
        # true_positives, false_negatives, false_positives, true_negatives
        self.assertEqual(values, (0,0,2,2))

    def test_calculate_precision_and_recall_no_true_positives(self):
        relevance_calculator = RelevanceCalculator(mock_topic(), test_model_name)
        # true_positives, false_negatives, false_positives, true_negatives
        values = (0,0,2,2)
        precision, recall = relevance_calculator.calculate_precision_and_recall(values)
        self.assertEqual(precision, 0)
        self.assertEqual(recall, 0)

    def test_calculate_precision_and_recall_two_true_positives_two_true_negatives(self):
        relevance_calculator = RelevanceCalculator(mock_topic(), test_model_name)
        # true_positives, false_negatives, false_positives, true_negatives
        values = (2,0,0,2)
        precision, recall = relevance_calculator.calculate_precision_and_recall(values)
        self.assertEqual(precision, 1)
        self.assertEqual(recall, 1)

    def test_calculate_precision_and_recall_two_true_positives_two_false_negatives(self):
        relevance_calculator = RelevanceCalculator(mock_topic(), test_model_name)
        # true_positives, false_negatives, false_positives, true_negatives
        values = (2,2,0,0)
        precision, recall = relevance_calculator.calculate_precision_and_recall(values)
        self.assertEqual(precision, 1)
        self.assertEqual(recall, 0.5)

    def test_get_relevance_metrics_no_true_positives(self):
        topic, annotations = mock_topic_annotations(annotations_examples["agreement"])
        relevance_calculator = RelevanceCalculator(topic, test_model_name)
        precision, recall = relevance_calculator.get_relevance_metrics(annotations)
        self.assertEqual(precision, 0)
        self.assertEqual(recall, 0)

    def test_get_relevance_metrics_two_true_positives_two_false_negatives(self):
        topic, annotations = mock_topic_annotations(annotations_examples["agreement"])
        mock_topic_cluster(topic, num_cluster=0)
        relevance_calculator = RelevanceCalculator(topic, test_model_name)
        precision, recall = relevance_calculator.get_relevance_metrics(annotations)
        self.assertEqual(precision, 0.5)
        self.assertEqual(recall, 1)
