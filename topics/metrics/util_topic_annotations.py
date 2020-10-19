from topics_identifier.topic_clusters import get_topic_clusters


# Get a list of all the documents ids
def get_documents_ids(annotations_list):
    documents_ids = []
    for annotation in annotations_list:
        id = annotation.document.id
        if id not in documents_ids: documents_ids.append(id)
    return documents_ids

def get_documents_from_annotations(annotations):
    documents = []
    for a in annotations:
        if a.document not in documents:
            documents.append(a.document)
    return documents

def get_topic_clusters_numbers(topic):
    numbers = [ topic_cluster.cluster.number for topic_cluster in get_topic_clusters(topic) ]
    return numbers

def get_labels(annotations):
    documents_ids = get_documents_ids(annotations)
    labels = []
    for id in documents_ids:
        labels_true = 0
        labels_false = 0
        for a in annotations:
            if a.document.id==id:
                if a.label == True: labels_true += 1
                else: labels_false += 1
        labels.append(labels_true > labels_false)
    return labels
