from common.testing.validations_views import validate_page
from metrics.models import TopicAnnotation


def validate_processed_line(test, result, expected, is_news):
    test.assertEqual(result["thread_number"], expected["thread_number"])
    test.assertEqual(result["content"], expected["content"])
    test.assertEqual(result["author"], expected["author"])
    test.assertEqual(result["date"], expected["date"])
    if is_news:
        test.assertEqual(result["title"], expected["title"])
        test.assertEqual(result["uri"], expected["uri"])

def validate_thread(test, thread, expected, is_news):
    test.assertEqual(thread.number, expected["thread_number"])
    if is_news:
        test.assertEqual(thread.title, expected["title"])
        test.assertEqual(thread.uri, expected["uri"])

def validate_document_with_thread(test, doc, expected, is_news):
    test.assertEqual(doc.content, expected["content"])
    test.assertEqual(doc.is_news, is_news)
    test.assertEqual(doc.author, expected["author"])
    test.assertEqual(doc.date, expected["date"])
    validate_thread(test, doc.thread, expected, is_news)

def validate_stored_annotation(test, topic, document, label, annotator):
    stored_annotations = TopicAnnotation.objects.all()
    test.assertEqual(len(stored_annotations), 1)
    test.assertEqual(stored_annotations[0].topic, topic)
    test.assertEqual(stored_annotations[0].document, document)
    test.assertEqual(stored_annotations[0].label, label)
    test.assertEqual(stored_annotations[0].annotator, annotator)
