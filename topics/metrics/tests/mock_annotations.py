import numpy as np
from metrics.models import TopicAnnotation
from .mocks import mock_threads_list, mock_topic


def mock_topic_annotations(annotators_labels=[[True,True,True,True]], topic_name="test_topic"):
    topic = mock_topic(topic_name)
    # Annotators labels is an array that contains the labels that each annotator has put to each thread.
    num_annotators = len(annotators_labels)
    # Mock as many threads as labels per annotator
    num_threads = len(annotators_labels[0])
    threads_list = mock_threads_list(num_threads)
    # Assign labels to threads
    annotations_list = []
    for t in range(num_threads):
        for a in range(num_annotators):
            thread = threads_list[t]
            label = annotators_labels[a][t]
            annotation = TopicAnnotation(topic=topic, thread=thread, label=label, annotator=a)
            annotation.save()
            annotations_list.append(annotation)
    return annotations_list

def mock_matrix(array):
    matrix = np.matrix(array)
    return matrix
