import numpy as np
from statsmodels.stats.inter_rater import fleiss_kappa
from .models import TopicAnnotation
from .util_topic_annotations import get_documents_ids


# Increase the counter corresponding to the document id and the label
def increase_annotation_counter(annotations_counter, id, label):
    for annotation in annotations_counter:
        # Find the counter corresponding to the document id
        if annotation["id"]==id:
            # increase counter[0] if label is True
            if label: annotation["counter"][0] += 1
            # increase counter[1] if label is False
            else: annotation["counter"][1] += 1
            continue

# Builds an array with an entry for each document id,
# that contains an array with a counter for each label.
def get_annotations_counter(annotations_list):
    documents_ids = get_documents_ids(annotations_list)
    # Creates an array with all the documents ids and a counter for each of the labels.
    annotations_counter = [{"id":id, "counter":[0,0]} for id in documents_ids]
    # Increase the label counter for each annotation
    for a in annotations_list:
        increase_annotation_counter(annotations_counter, a.document.id, a.label)
    # Transform into an array that only contains the counters.
    counters_array = [ a["counter"] for a in annotations_counter ]
    return counters_array

# Gets a Numpy matrix with shape: documents_ids x labels
# The matrix contains the number of times that each document is annotated with each label.
def get_annotations_matrix(annotations):
    annotations_counter = get_annotations_counter(annotations)
    matrix = np.matrix(annotations_counter)
    return matrix

def calculate_inter_annotator_agreement(annotations):
    matrix = get_annotations_matrix(annotations)
    fleiss_kappa_score = fleiss_kappa(matrix)
    return fleiss_kappa_score
