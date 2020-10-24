from timeline.models import Topic
from .mocks import mock_document


def mock_annotated_topic(annotation):
    title = annotation[0]
    content = title + "\n" + annotation[1]
    document = mock_document(content=content, is_news=True)
    document.save()
    topic_name = annotation[2]
    topic, _ = Topic.objects.get_or_create(name=topic_name)
    return topic, document
