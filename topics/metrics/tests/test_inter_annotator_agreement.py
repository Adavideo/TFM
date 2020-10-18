from django.test import TestCase
from metrics.inter_annotator_agreement import *
from .examples_annotations import annotations_examples
from .mock_annotations import mock_topic_annotations, mock_matrix
from .mocks import mock_topic, mock_thread_with_news


class InterAnnotatorAgreementTests(TestCase):

    def test_get_threads_ids(self):
        _, annotations_list = mock_topic_annotations()
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
        _, annotations_list = mock_topic_annotations(annotators_labels)
        # Execute
        counters_array = get_annotations_counter(annotations_list)
        # Validate
        expected_array = [[2, 0], [0, 2], [0, 2], [2, 0]]
        self.assertEqual(counters_array, expected_array)

    def test_get_annotations_counter_two_threads_with_same_title(self):
        # Initialize
        topic = mock_topic('Renta basica')
        title = 'El Gobierno trabaja en una renta mínima vital que beneficiará a más de 5 millones de ciudadanos frente al Covid-19'
        content0 = 'El Gobierno está trabajando en una renta mínima vital de la que se beneficiaría más de 5 millones de ciudadanos en España para hacer frente a la crisis provocada por el coronavirus COVID-19, según ha anunciado el vicepresidente de Derechos Sociales y Agenda 2030, Pablo Iglesias'
        content1 = 'Diferent content'
        input_annotation0 = [title, content0, topic.name, 'x', '1']
        input_annotation1 = [title, content1, topic.name, 'x', '2']
        #thread0 = mock_thread_for_annotated_topic(input_annotation0, topic.name, thread_number=0)
        thread0 = mock_thread_with_news(title, content0, thread_number=0)
        thread1 = mock_thread_with_news(title, content1, thread_number=1)
        annotation0 = TopicAnnotation(topic=topic, thread=thread0, label=True, annotator=1)
        annotation0.save()
        annotation1 = TopicAnnotation(topic=topic, thread=thread0, label=True, annotator=2)
        annotation1.save()
        annotation2 = TopicAnnotation(topic=topic, thread=thread1, label=True, annotator=1)
        annotation2.save()
        annotation3 = TopicAnnotation(topic=topic, thread=thread1, label=True, annotator=2)
        annotation3.save()
        annotations_list = [annotation0, annotation1, annotation2, annotation3]
        # Execute
        counters_array = get_annotations_counter(annotations_list)
        # Validate
        expected_array = [[2, 0], [2, 0]]
        self.assertEqual(counters_array, expected_array)

    def test_get_annotations_matrix(self):
        # Initialize
        topic, annotations_list = mock_topic_annotations(annotations_examples["agreement"])
        # Execute
        matrix = get_annotations_matrix(annotations_list)
        # Validate
        num_threads, num_labels = matrix.shape
        self.assertEqual(num_threads, 4)
        self.assertEqual(num_labels, 2)
        num_annotators = np.sum(matrix[0, :])
        self.assertEqual(num_annotators, 3)

    def test_calculate_inter_annotator_agreement_total_agreement(self):
        # Initialize
        topic, annotations_list = mock_topic_annotations(annotations_examples["agreement"])
        # Execute
        score = calculate_inter_annotator_agreement(annotations_list)
        # Validate
        self.assertEqual(score, 1.0)

    def test_calculate_inter_annotator_agreement_small_disagreement(self):
        # Initialize
        topic, annotations_list = mock_topic_annotations(annotations_examples["small disagreement"])
        # Execute
        score = calculate_inter_annotator_agreement(annotations_list)
        # Validate
        self.assertEqual(score, 0.6571428571428569)

    def test_calculate_inter_annotator_agreement_big_disagreement(self):
        # Initialize
        topic, annotations_list = mock_topic_annotations(annotations_examples["big disagreement"])
        # Execute
        score = calculate_inter_annotator_agreement(annotations_list)
        # Validate
        self.assertEqual(score, -0.33333333333333337)
