from .TreeGenerator import TreeGenerator
from .models import Topic, Cluster, ClusterTopic


def build_tree_generator(request, level):
    tree_name = request.POST["tree_name"]
    model_name = request.POST["model_name"]
    document_types = request.POST["document_types"]
    documents_options = { "types": document_types,
                          "max_num_documents": None,
                          "batches": True }
    tree_generator = TreeGenerator(tree_name, model_name, documents_options, max_level=level)
    return tree_generator

def get_topic_clusters_with_documents(topic):
    topic_clusters = ClusterTopic.objects.filter(topic=topic)
    list = [ { "cluster": i.cluster, "documents": i.cluster.documents()} for i in topic_clusters ]
    return list

def assign_topic_to_clusters(request):
    # Get topic
    topic_id = request.POST["topic"]
    topic = Topic.objects.get(id=topic_id)
    # Get clusters
    clusters_ids = request.POST.getlist("selected_clusters")
    clusters_list = [ Cluster.objects.get(id=id) for id in clusters_ids ]
    # Assign topic to clusters
    for cluster in clusters_list:
        ClusterTopic.objects.get_or_create(cluster=cluster, topic=topic)
    return topic, clusters_list
