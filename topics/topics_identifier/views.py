from django.shortcuts import render
from .forms import *
from .csv_importer import process_csv
from .data_importer import load_and_store_dataset
from .data_classifier import cluster_data

def index_view(request):
    template = "topics_identifier/home.html"
    context = {}
    return render(request, template, context)

def import_files_view(request):
    template = "topics_identifier/file_upload.html"
    form = ImportCSVForm()
    context = {'form': form }
    if request.method == "POST":
        file = request.FILES['file']
        context["result"] = process_csv(file)
    return render(request, template, context)

def generate_dataset_view(request):
    template = "topics_identifier/generate_dataset.html"
    dataset = load_and_store_dataset()
    context = { "result": dataset }
    return render(request, template, context)

def cluster_data_view(request):
    template = "topics_identifier/cluster_data.html"
    form = ClusterForm(request.POST)
    context = {'form': form }
    if request.method == "POST":
        dataset_name = request.POST["dataset_name"]
        context["clusters"] = cluster_data(dataset_name)
    return render(request, template, context )
