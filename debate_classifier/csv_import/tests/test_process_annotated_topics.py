from django.test import TestCase
from metrics.models import TopicAnnotation
from csv_import.csv_importer import process_topic_annotation, process_csv_line
from .examples_topic_annotations import example_topic_annotations1
#from .mocks import mock_document
from .mocks_for_annotated_topics import mock_annotated_topic
from .validations import validate_stored_annotation


class ProcessDataAnnotatedTopicsTests(TestCase):

    def test_process_topic_annotation_true(self):
        # Initialize
        annotation = example_topic_annotations1["processed"][0]
        topic, document = mock_annotated_topic(annotation)
        # Execute
        result = process_topic_annotation(annotation)
        # Validate
        self.assertEqual(result["content"], annotation[1])
        validate_stored_annotation(self, topic, document, label=True, annotator=1)

    def test_process_topic_annotation_false(self):
        # Initialize
        annotation = example_topic_annotations1["processed"][1]
        topic, document = mock_annotated_topic(annotation)
        # Execute
        result = process_topic_annotation(annotation)
        # Validate
        self.assertEqual(result["title"], annotation[0])
        self.assertEqual(result["content"], annotation[1])
        validate_stored_annotation(self, topic, document, label=False, annotator=1)

    def test_process_csv_line_topic_annotation(self):
        # Initialize
        annotation = example_topic_annotations1["processed"][0]
        topic, document = mock_annotated_topic(annotation)
        # Execute
        result = process_csv_line(annotation, file_type="topic_annotations")
        # Validate
        self.assertEqual(result["title"], annotation[0])
        self.assertEqual(result["content"], annotation[1])
        validate_stored_annotation(self, topic, document, label=True, annotator=1)
