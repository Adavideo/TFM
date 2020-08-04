from django.shortcuts import render
from .forms import *
from .TreeGenerator import TreeGenerator, tree_already_exist
from .clusters_search import cluster_search
from .clusters_navigation import compose_cluster_information
from .models import Cluster, Tree
from .renta_basica import get_documents

def renta_basica_view(request):
    template = "topics_identifier/renta_basica.html"
    news_texts = get_documents()
    context = { "list": news_texts }
    return render(request, template, context)

def generate_tree_view(request):
    level = 1
    template = "topics_identifier/generate_tree.html"
    form = TreeForm(request.POST)
    context = { "form": form }
    if request.method == "POST":
        tree_name = request.POST["tree_name"]
        if tree_already_exist(tree_name):
            context["message"] = "Tree name already in use. Pick a different one."
            return render(request, template, context)
        document_types = request.POST["document_types"]
        # Cluster the documents in two levels and store them in a cluster tree
        generator = TreeGenerator(tree_name, document_types=document_types, max_level=level)
        tree = generator.generate_tree()
        # Prepare the information to show on the web page
        level1_clusters = tree.get_clusters_of_level(level)
        context["num_clusters"] = len(level1_clusters)
        context["clusters"] = level1_clusters
        context["tree_name"] = tree_name
    return render(request, template, context)

def cluster_view(request, cluster_id):
    template = "topics_identifier/cluster_page.html"
    cluster = Cluster.objects.get(id=cluster_id)
    cluster_info = compose_cluster_information(cluster, include_documents=True)
    context = { "cluster_info": cluster_info }
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
        context["clusters"] = clusters
    return render(request, template, context)

def trees_index_view(request):
    template = "topics_identifier/trees_index.html"
    trees = Tree.objects.all()
    context = { "trees_list": trees }
    return render(request, template, context)
