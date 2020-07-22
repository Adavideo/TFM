from django.shortcuts import render
from .forms import *
from .csv_importer import process_csv
from .generate_clusters import cluster_level
from .clusters_navigation import get_tree, get_trees_list, compose_tree, cluster_search
from .models import Cluster

def index_view(request):
    template = "topics_identifier/home.html"
    context = {}
    return render(request, template, context)

def import_files_view(request):
    template = "topics_identifier/import_csv.html"
    form = ImportCSVForm()
    context = {'form': form }
    if request.method == "POST":
        file = request.FILES['file']
        registers = process_csv(file)
        context["registers"] = registers[:100]
        context["num_registers"] = len(registers)
    return render(request, template, context)

def generate_clusters_level0_view(request):
    level = 0
    template = "topics_identifier/generate_clusters.html"
    form = ClusterForm(request.POST)
    context = { "form": form }
    if request.method == "POST":
        tree_name = request.POST["tree_name"]
        context["tree_name"] = tree_name
        # Form clusters with the documents on the tree
        cluster_level(tree_name, level=level)
        # Prepare the information to show on the web page
        all_clusters = Cluster.objects.filter(tree_name=tree_name, level=level)
        context["clusters"] = all_clusters[:100]
        num_clusters = len(all_clusters)
        context["num_clusters"] = num_clusters
    return render(request, template, context )

def generate_clusters_level1_view(request):
    level = 1
    template = "topics_identifier/generate_clusters_2_levels.html"
    form = ClusterForm(request.POST)
    context = { "form": form }
    if request.method == "POST":
        tree_name = request.POST["tree_name"]
        # Form clusters with the documents on the tree
        cluster_level(tree_name, level=level)
        # Prepare the information to show on the web page
        all_clusters = Cluster.objects.filter(tree_name=tree_name, level=level)
        context["num_clusters"] = len(all_clusters)
        context["clusters"] = all_clusters
        context["tree_name"] = tree_name
    return render(request, template, context )

def cluster_view(request, cluster_id):
    template = "topics_identifier/cluster_page.html"
    cluster = Cluster.objects.get(id=cluster_id)
    cluster_tree = compose_tree([cluster], include_documents=True)
    context = { "cluster_info": cluster_tree[0] }
    return render(request, template, context )

def clusters_tree_view(request, tree_name=None):
    template = "topics_identifier/clusters_trees.html"
    form = ClusterSeachForm()
    context = {"tree_name": tree_name, 'form': form }
    if request.method == "POST":
        search_string = request.POST["search_terms"]
        context["search_string"] = search_string
        context["trees"] = cluster_search(tree_name, search_string)
    else:
        clusters_tree = get_tree(tree_name, include_documents=False)
        context["trees"] = [ clusters_tree ]
    return render(request, template, context )

def clusters_index_view(request):
    template = "topics_identifier/clusters_index.html"
    trees = get_trees_list()
    context = { "trees_list": trees }
    return render(request, template, context )
