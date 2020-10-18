from django.test import TestCase
from timeline.models import Thread
from metrics.models import TopicAnnotation
from csv_import.csv_importer import find_thread, process_topic_annotation, process_csv_line
from .examples_topic_annotations import example_topic_annotations1
from .mocks import mock_thread
from .mocks_for_annotated_topics import *
from .validations import validate_stored_annotation


class ProcessDataAnnotatedTopicsTests(TestCase):

    def test_find_thread_using_title(self):
        mocked_thread = mock_thread(thread_number=0)
        thread = find_thread(title=mocked_thread.title, content="")
        self.assertEqual(thread, mocked_thread)

    # When there is two news with same title but diferent content,
    # we need to use the content to find the correct thread
    def test_find_thread_using_news_content(self):
        # Initialize
        title = "A title"
        mocked_thread0 = mock_thread_with_news(title, content="content0", thread_number=0)
        mocked_thread1 = mock_thread_with_news(title, content="content1", thread_number=1)
        # Execute
        thread0 = find_thread(title=title, content="content0")
        thread1 = find_thread(title=title, content="content1")
        # Validate
        self.assertEqual(thread0, mocked_thread0)
        self.assertEqual(thread1, mocked_thread1)

    def test_process_topic_annotation_true(self):
        # Initialize
        topic_name = example_topic_annotations1["topic_name"]
        annotation = example_topic_annotations1["processed"][0]
        thread = mock_thread_for_annotated_topic(annotation, topic_name)
        # Execute
        result = process_topic_annotation(annotation)
        # Validate
        self.assertEqual(result["title"], annotation[0])
        self.assertEqual(result["content"], annotation[1])
        validate_stored_annotation(self, topic_name, thread, label=True, annotator=1)

    def test_process_topic_annotation_false(self):
        # Initialize
        topic_name = example_topic_annotations1["topic_name"]
        annotation = example_topic_annotations1["processed"][1]
        thread = mock_thread_for_annotated_topic(annotation, topic_name)
        # Execute
        result = process_topic_annotation(annotation)
        # Validate
        self.assertEqual(result["title"], annotation[0])
        self.assertEqual(result["content"], annotation[1])
        validate_stored_annotation(self, topic_name, thread, label=False, annotator=1)

    def test_process_topic_annotation_two_annotations_with_same_title(self):
        # Initialize
        topic_name = 'Renta basica'
        title = 'El Gobierno trabaja en una renta mínima vital que beneficiará a más de 5 millones de ciudadanos frente al Covid-19'
        content0 = 'El Gobierno está trabajando en una renta mínima vital de la que se beneficiaría más de 5 millones de ciudadanos en España para hacer frente a la crisis provocada por el coronavirus COVID-19, según ha anunciado el vicepresidente de Derechos Sociales y Agenda 2030, Pablo Iglesias'
        content1 = 'Diferent content'
        annotation0 = [title, content0, topic_name, 'x', '1']
        annotation1 = [title, content1, topic_name, 'x', '2']
        mock_thread_for_annotated_topic(annotation0, topic_name, thread_number=0)
        mock_thread_for_annotated_topic(annotation1, topic_name, thread_number=1)
        # Execute
        process_topic_annotation(annotation0)
        process_topic_annotation(annotation1)
        # Validate
        stored_annotations = TopicAnnotation.objects.all()
        thread0 = stored_annotations[0].thread
        thread1 = stored_annotations[1].thread
        self.assertEqual(thread0.title, title)
        self.assertEqual(thread0.news().content, title+"\n"+content0)
        self.assertEqual(thread1.title, title)
        self.assertEqual(thread1.news().content, title+"\n"+content1)
        self.assertEqual(stored_annotations[0].label, True)
        self.assertEqual(stored_annotations[1].label, True)
        self.assertEqual(stored_annotations[0].annotator, 1)
        self.assertEqual(stored_annotations[1].annotator, 2)

    def test_process_csv_line_topic_annotation(self):
        # Initialize
        topic_name = example_topic_annotations1["topic_name"]
        annotation = example_topic_annotations1["processed"][0]
        thread = mock_thread_for_annotated_topic(annotation, topic_name)
        # Execute
        result = process_csv_line(annotation, file_type="topic_annotations")
        # Validate
        self.assertEqual(result["title"], annotation[0])
        self.assertEqual(result["content"], annotation[1])
        validate_stored_annotation(self, topic_name, thread, label=True, annotator=1)
