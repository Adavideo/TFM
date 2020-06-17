from django.shortcuts import render
from .forms import *
from .csv_importer import process_csv
from .datasets_manager import load_and_store_dataset, load_dataset
from .texts_documents_manager import short_texts_filenames
from .clustering import cluster_data
from .clusters_navigation import get_clusters_with_documents, get_datasets_clusters_list
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

def cluster_data_view(request):
    template = "topics_identifier/cluster_data.html"
    form = ClusterForm(request.POST)
    context = { "form": form }
    if request.method == "POST":
        # Load the dataset
        dataset_name = request.POST["dataset_name"]
        dataset = load_dataset(dataset_name)
        # Form clusters with the documents on the dataset
        cluster_data(dataset, dataset_name)
        # Prepare the information to show on the web page
        context["clusters"] = Cluster.objects.filter(dataset=dataset_name)
        dataset_info = { "name": dataset_name, "description": dataset.DESCR }
        context["dataset_info"] = dataset_info
    return render(request, template, context )

def clusters_view(request, dataset_name=None):
    template = "topics_identifier/clusters.html"
    clusters_list = get_clusters_with_documents(dataset_name)
    context = {"clusters_list": clusters_list, "dataset_name": dataset_name }
    return render(request, template, context )

def clusters_index_view(request):
    template = "topics_identifier/clusters_index.html"
    clusters_list = get_datasets_clusters_list()
    context = { "datasets_clusters_list": clusters_list }
    return render(request, template, context )
