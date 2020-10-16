from django.test import TestCase
from metrics.inter_annotator_agreement import *
from .examples_annotations import annotations_examples
from .mock_annotations import *


class InterAnnotatorAgreementTests(TestCase):

    def test_get_threads_ids(self):
        annotations_list = mock_topic_annotations()
        threads_ids = get_threads_ids(annotations_list)
        self.assertEqual(threads_ids, [1, 2, 3, 4])

    def test_increase_annotation_counter(self):
        annotations_counter = [{"id":1, "counter":[1, 1]}, {"id":1, "counter":[0, 0]}]
        increase_annotation_counter(annotations_counter, id=1, label=True)
        expected = [{'counter': [2, 1], 'id': 1}, {'counter': [1, 0], 'id': 1}]
        self.assertEqual(annotations_counter, expected)

    def test_get_annotations_counter(self):
        # Initialize
        annotator1 = [True, False, False, True]
        annotator2 = [True, False, False, True]
        annotators_labels = [annotator1, annotator2]
        annotations_list = mock_topic_annotations(annotators_labels)
        # Execute
        counters_array = get_annotations_counter(annotations_list)
        # Validate
        expected_array = [[2, 0], [0, 2], [0, 2], [2, 0]]
        self.assertEqual(counters_array, expected_array)

    def test_get_annotations_matrix(self):
        # Initialize
        annotations_list = mock_topic_annotations(annotations_examples["agreement"])
        topic = annotations_list[0].topic
        # Execute
        matrix = get_annotations_matrix(topic)
        # Validate
        num_threads, num_labels = matrix.shape
        self.assertEqual(num_threads, 4)
        self.assertEqual(num_labels, 2)
        num_annotators = np.sum(matrix[0, :])
        self.assertEqual(num_annotators, 3)

    def test_calculate_inter_annotator_agreement_total_agreement(self):
        # Initialize
        annotations_list = mock_topic_annotations(annotations_examples["agreement"])
        topic = annotations_list[0].topic
        # Execute
        score = calculate_inter_annotator_agreement(topic)
        # Validate
        self.assertEqual(score, 1.0)

    def test_calculate_inter_annotator_agreement_small_disagreement(self):
        # Initialize
        annotations_list = mock_topic_annotations(annotations_examples["small disagreement"])
        topic = annotations_list[0].topic
        # Execute
        score = calculate_inter_annotator_agreement(topic)
        # Validate
        self.assertEqual(score, 0.6571428571428569)

    def test_calculate_inter_annotator_agreement_big_disagreement(self):
        # Initialize
        annotations_list = mock_topic_annotations(annotations_examples["big disagreement"])
        topic = annotations_list[0].topic
        # Execute
        score = calculate_inter_annotator_agreement(topic)
        # Validate
        self.assertEqual(score, -0.33333333333333337)
