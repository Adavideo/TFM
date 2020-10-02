from django.shortcuts import render
from .forms import *
from .clusters_search import cluster_search
from .clusters_navigation import compose_cluster_information
from .models import Cluster, Tree, ClusterTopic
from .topic_assign_from_file import assign_topic_from_file
from .topic_clusters import get_topic_clusters_with_documents
from .views_util import *


def home_view(request):
    template = "topics_identifier/topics_identifier_home.html"
    context = {}
    return render(request, template, context)

def generate_tree_view(request):
    level = 1
    template = "topics_identifier/generate_tree.html"
    form = TreeForm(request.POST)
    context = { "form": form }
    if request.method == "POST":
        tree_generator = build_tree_generator(request, level)
        if tree_generator.tree_already_exist:
            context["message"] = "Tree name already in use. Pick a different one."
        else:
            context["tree_name"] = request.POST["tree_name"]
            clusters = tree_generator.generate_tree()
            context["num_clusters"] = len(clusters)
            context["clusters_list"] = clusters
    return render(request, template, context)

def trees_index_view(request):
    template = "topics_identifier/trees_index.html"
    trees = Tree.objects.all()
    context = { "trees_list": trees }
    return render(request, template, context)

def tree_view(request, tree_id):
    template = "topics_identifier/tree_page.html"
    tree = Tree.objects.get(id=tree_id)
    context = { "tree": tree }
    if request.method == "GET":
        context["form"] = ClusterSeachForm()
        context["clusters_list"] = tree.get_max_level_clusters()
    if request.method == "POST":
        search_string = request.POST["search_terms"]
        context["search_string"] = search_string
        search_results = cluster_search(tree, search_string)
        context["search_results"] = search_results
        context["form"] = AssignTopicToClustersForm(request.POST, search_results=search_results)
    return render(request, template, context)

def cluster_view(request, cluster_id):
    template = "topics_identifier/cluster_page.html"
    cluster = Cluster.objects.get(id=cluster_id)
    cluster_info = compose_cluster_information(cluster, include_documents=True)
    context = { "cluster_info": cluster_info }
    return render(request, template, context)

def topics_index_view(request):
    template = "topics_identifier/topics_index.html"
    topics_list = Topic.objects.all()
    context = { "topics_list": topics_list }
    return render(request, template, context)

def topic_view(request, topic_id):
    template = "topics_identifier/topic_page.html"
    topic = Topic.objects.get(id=topic_id)
    documents = topic.get_documents(type="news")
    context = { "topic": topic, "documents": documents }
    return render(request, template, context)

def topic_clusters_view(request, topic_id):
    template = "topics_identifier/topic_clusters.html"
    topic = Topic.objects.get(id=topic_id)
    clusters_with_documents = get_topic_clusters_with_documents(topic)
    context = { "topic": topic, "clusters_with_documents": clusters_with_documents }
    return render(request, template, context)

def assign_topic_to_clusters_view(request):
    template = "topics_identifier/assigned_topic_to_clusters.html"
    topic, clusters_list = assign_topic_to_clusters(request)
    context = { "selected_clusters": clusters_list, "topic": topic }
    return render(request, template, context)

def label_documents_view(request, topic_id):
    template = "topics_identifier/label_documents.html"
    topic = Topic.objects.get(id=topic_id)
    if request.method == "GET":
        documents = get_documents_to_label(topic)
        documents_choices = prepare_documents_for_select_field(documents)
        form = AssignTopicToDocumentsForm(request.POST, documents=documents_choices)
        context = { "topic": topic, "form": form }
    else:
        selected_documents = get_selected_documents(request)
        for doc in selected_documents:
            doc.assign_topic(topic)
        context = { "topic": topic, "documents": selected_documents }
    return render(request, template, context)

def assign_topic_from_file_view(request):
    template = "topics_identifier/assign_topic_from_file.html"
    form = AssignTopicFromFileForm(request.POST)
    context = { "form": form }
    if request.method == "POST":
        topic_name = request.POST["topic_name"]
        threads_list = assign_topic_from_file(topic_name)
        context["threads_list"] = threads_list
    return render(request, template, context)
