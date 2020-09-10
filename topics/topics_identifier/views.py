from django.shortcuts import render
from .forms import *
from .clusters_search import cluster_search
from .clusters_navigation import compose_cluster_information
from .models import Cluster, Tree
from .topics_clustering import cluster_for_topic
from .topics_assignations import assign_topic_from_file
from .ModelsManager import ModelsManager
from .TreeGenerator import TreeGenerator
from .documents_selector import select_documents


def home_view(request):
    template = "topics_identifier/topics_identifier_home.html"
    context = {}
    return render(request, template, context)

def generate_model_view(request):
    template = "topics_identifier/generate_model.html"
    form = ModelsForm(request.POST)
    context = { "form": form }
    if request.method == "POST":
        model_name = request.POST["model_name"]
        context["model_name"] = model_name
        document_types = request.POST["document_types"]
        documents_options = { "types": document_types}
        max_level=1
        documents = select_documents(documents_options)
        models_manager = ModelsManager(name=model_name)
        model_filename = models_manager.generate_and_store_models(documents, max_level)
        context["model_filename"] = model_filename
    return render(request, template, context)

def generate_tree_view(request):
    level = 1
    template = "topics_identifier/generate_tree.html"
    form = TreeForm(request.POST)
    context = { "form": form }
    if request.method == "POST":
        tree_name = request.POST["tree_name"]
        model_name = request.POST["model_name"]
        document_types = request.POST["document_types"]
        documents_options = { "types": document_types }
        tree_generator = TreeGenerator(tree_name, model_name, documents_options, max_level=level)
        if tree_generator.tree_already_exist:
            context["message"] = "Tree name already in use. Pick a different one."
        else:
            context["tree_name"] = tree_name
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
    template = "topics_identifier/tree.html"
    tree = Tree.objects.get(id=tree_id)
    form = ClusterSeachForm()
    context = { "tree": tree, 'form': form }
    if request.method == "POST":
        search_string = request.POST["search_terms"]
        context["search_string"] = search_string
        context["search_results"] = cluster_search(tree, search_string)
    else:
        clusters = tree.get_clusters_of_level(1)
        if not clusters: clusters = tree.get_clusters_of_level(0)
        context["clusters_list"] = clusters
    return render(request, template, context)

def cluster_view(request, cluster_id):
    template = "topics_identifier/cluster_page.html"
    cluster = Cluster.objects.get(id=cluster_id)
    cluster_info = compose_cluster_information(cluster, include_documents=True)
    context = { "cluster_info": cluster_info }
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

def cluster_topic_view(request):
    template = "topics_identifier/clusters_on_topic.html"
    form = ClusterTopicForm(request.POST)
    context = { "form": form }
    if request.method == "POST":
        topic_id = request.POST["topic"]
        topic = Topic.objects.get(id=topic_id)
        context["topic"] = topic.name
        model_name = request.POST["model_name"]
        context["model_name"] = model_name
        context["clusters_list"] = cluster_for_topic(topic, model_name)
    return render(request, template, context)
