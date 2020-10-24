from timeline.models import Topic


def mock_topic(name="test_topic"):
    topic = Topic(name=name)
    topic.save()
    return topic
