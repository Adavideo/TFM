from .models import ClusterTopic, Document


def get_topic_clusters(topic):
    return ClusterTopic.objects.filter(topic=topic)

def get_topic_clusters_with_documents(topic):
    topic_clusters = get_topic_clusters(topic)
    list = [ { "cluster": i.cluster, "documents": i.cluster.documents()} for i in topic_clusters ]
    return list

def get_clusters_documents(topic):
    topic_clusters = get_topic_clusters(topic)
    clusters_documents = []
    for i in topic_clusters:
        clusters_documents.extend( i.cluster.documents() )
    return clusters_documents

def get_labeled_documents(topic):
    topic_threads = topic.get_threads()
    documents = [ Document.objects.get(thread=thread, is_news=True) for thread in topic_threads ]
    return documents

def get_documents_to_label(topic):
    clusters_documents = get_clusters_documents(topic)
    labeled_documents = get_labeled_documents(topic)
    documents_to_label = list( set(clusters_documents) - set(labeled_documents) )
    return documents_to_label
