import numpy as np
from topics_identifier.tests.mock_clusters import mock_cluster
from topics_identifier.models import ClusterTopic
from metrics.models import TopicAnnotation
from .mocks import mock_documents, mock_topic


def mock_topic_annotations(annotators_labels=[[True,True,True,True]], topic_name="test_topic"):
    topic = mock_topic(topic_name)
    # Annotators labels is an array that contains the labels that each annotator has put to each document.
    num_annotators = len(annotators_labels)
    # Mock as many documents as labels per annotator
    num_documents = len(annotators_labels[0])
    documents_list = mock_documents(is_news=True)
    # Assign labels to documents
    annotations_list = []
    for t in range(num_documents):
        for a in range(num_annotators):
            document = documents_list[t]
            label = annotators_labels[a][t]
            annotation = TopicAnnotation(topic=topic, document=document, label=label, annotator=a)
            annotation.save()
            annotations_list.append(annotation)
    return topic, annotations_list

def mock_matrix(array):
    matrix = np.matrix(array)
    return matrix

def mock_topic_cluster(topic, num_cluster):
    cluster = mock_cluster(num_cluster=num_cluster)
    cluster_topic = ClusterTopic(topic=topic, cluster=cluster)
    cluster_topic.save()
