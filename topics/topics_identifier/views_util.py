from .TreeGenerator import TreeGenerator
from .models import Topic, Cluster, Document, ClusterTopic
from .topic_clusters import get_documents_to_label


def build_tree_generator(request, level):
    tree_name = request.POST["tree_name"]
    model_name = request.POST["model_name"]
    document_types = request.POST["document_types"]
    documents_options = { "types": document_types,
                          "max_num_documents": None,
                          "batches": True }
    tree_generator = TreeGenerator(tree_name, model_name, documents_options, max_level=level)
    return tree_generator

def prepare_documents_for_select_field(documents):
    choices = [ (doc.id, doc.content) for doc in documents ]
    return choices

def get_selected_documents(request):
    documents_ids = request.POST.getlist("documents")
    documents = [ Document.objects.get(id=id) for id in documents_ids ]
    return documents

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
