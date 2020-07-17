from django.shortcuts import render
from .forms import *
from .csv_importer import process_csv
from .datasets_manager import load_and_store_dataset
from .texts_documents_manager import short_texts_filenames
from .generate_clusters import cluster_data, cluster_level
from .clusters_navigation import get_clusters_information, get_datasets_clusters_list
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

def generate_dataset_view(request):
    template = "topics_identifier/generate_dataset.html"
    form = GenerateDatasetForm(request.POST)
    context = { "form": form }
    if request.method == "POST":
        dataset_name = request.POST["dataset_name"]
        description = request.POST["description"]
        # Generate the dataset from text files and store it
        dataset = load_and_store_dataset(dataset_name, description)
        # Prepare the information to show on the web page
        documents = dataset.data[:100] # Showing only the first 100 documents
        dataset_info = { "name": dataset_name, "description": description,
                         "num_documents": len(dataset.data), "documents": documents  }
        context["dataset_info"] = dataset_info
        # cuts the path from the filenames to make them shorter
        short_filenames = short_texts_filenames(dataset.filenames)
        context["files"] = { "number": len(dataset.filenames), "list": short_filenames }
    return render(request, template, context)

def generate_clusters_level0_view(request):
    level = 0
    template = "topics_identifier/generate_clusters.html"
    form = ClusterForm(request.POST)
    context = { "form": form }
    if request.method == "POST":
        dataset_name = request.POST["dataset_name"]
        # Form clusters with the documents on the dataset
        cluster_level(dataset_name, level=level)
        # Prepare the information to show on the web page
        all_clusters = Cluster.objects.filter(dataset=dataset_name, level=level)
        num_clusters = len(all_clusters)
        context["num_clusters"] = num_clusters
        context["clusters"] = all_clusters[:100]
        dataset_info = { "name": dataset_name }
        context["dataset_info"] = dataset_info
    return render(request, template, context )

def generate_clusters_level1_view(request):
    level = 1
    template = "topics_identifier/generate_clusters_2_levels.html"
    form = ClusterForm(request.POST)
    context = { "form": form }
    if request.method == "POST":
        dataset_name = request.POST["dataset_name"]
        # Form clusters with the documents on the dataset
        cluster_level(dataset_name, level=level)
        # Prepare the information to show on the web page
        all_clusters = Cluster.objects.filter(dataset=dataset_name, level=level)
        context["num_clusters"] = len(all_clusters)
        context["clusters"] = all_clusters
        context["dataset_name"] = dataset_name
    return render(request, template, context )

def clusters_view(request, dataset_name=None):
    template = "topics_identifier/clusters.html"
    clusters_list = get_clusters_information(dataset_name, include_children=True)
    context = {"clusters_list": clusters_list, "dataset_name": dataset_name }
    return render(request, template, context )

def clusters_index_view(request):
    template = "topics_identifier/clusters_index.html"
    clusters_list = get_datasets_clusters_list()
    context = { "datasets_clusters_list": clusters_list }
    return render(request, template, context )
