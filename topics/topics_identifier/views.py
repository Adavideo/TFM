from django.shortcuts import render
from .forms import *
from .csv_importer import process_csv
from .data_importer import load_and_store_dataset
from .input_output_files import load_dataset
from .data_classifier import cluster_data

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
        context["result"] = process_csv(file)
    return render(request, template, context)

def generate_dataset_view(request):
    template = "topics_identifier/generate_dataset.html"
    form = GenerateDatasetForm(request.POST)
    context = { "form": form }
    if request.method == "POST":
        dataset_name = request.POST["dataset_name"]
        description = request.POST["description"]
        dataset = load_and_store_dataset(dataset_name, description)
        context["dataset_name"] = dataset_name
        context["result"] = dataset
    return render(request, template, context)

def cluster_data_view(request):
    template = "topics_identifier/cluster_data.html"
    form = ClusterForm(request.POST)
    context = {'form': form }
    if request.method == "POST":
        dataset_name = request.POST["dataset_name"]
        context["dataset_name"] = dataset_name
        dataset = load_dataset(dataset_name)
        if dataset:
            context["clusters"] = cluster_data(dataset)
            context["dataset_description"] = dataset.DESCR
    return render(request, template, context )
