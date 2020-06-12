from django.shortcuts import render
from .forms import *
from .csv_importer import process_csv
from .data_importer import load_and_store_dataset
from .input_output_files import load_dataset, short_texts_filenames
from .data_classifier import cluster_data
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
        dataset = load_and_store_dataset(dataset_name, description)
        context["dataset_name"] = dataset_name
        context["documents"] = dataset.data[:100]
        context["num_documents"] = len(dataset.data)
        # cuts the path from the filenames to make them shorter
        short_filenames = short_texts_filenames(dataset.filenames)
        context["files"] = short_filenames
        context["num_files"] = len(dataset.filenames)
    return render(request, template, context)

def cluster_data_view(request):
    template = "topics_identifier/cluster_data.html"
    form = ClusterForm(request.POST)
    context = {'form': form }
    if request.method == "POST":
        dataset_name = request.POST["dataset_name"]
        context["dataset_name"] = dataset_name
        dataset = load_dataset(dataset_name)
        context["dataset_description"] = dataset.DESCR
        cluster_data(dataset, dataset_name)
        context["clusters"] = Cluster.objects.filter(dataset=dataset_name)
    return render(request, template, context )

def clusters_view(request, dataset_name=None):
    if dataset_name:
        clusters = Cluster.objects.filter(dataset=dataset_name)
    else:
        clusters = Cluster.objects.all()
    clusters_list = []
    for cluster in clusters:
        docs = cluster.documents()
        cluster_info = {"cluster": cluster, "documents": docs}
        clusters_list.append(cluster_info)

    template = "topics_identifier/clusters.html"
    context = {"clusters_list": clusters_list, "dataset_name": dataset_name }
    return render(request, template, context )

def get_datasets_names():
    datasets_names = []
    for cluster in Cluster.objects.all():
        if cluster.dataset not in datasets_names:
            datasets_names.append(cluster.dataset)
    return datasets_names

def get_datasets_clusters_list():
    datasets_names = get_datasets_names()
    datasets_list = []
    for dataset_name in datasets_names:
        num_clusters = len(Cluster.objects.filter(dataset=dataset_name))
        info = { "dataset_name": dataset_name, "num_clusters": num_clusters }
        datasets_list.append(info)
    return datasets_list

def clusters_index_view(request):
    context = { "datasets_clusters_list": get_datasets_clusters_list() }
    template = "topics_identifier/clusters_index.html"
    return render(request, template, context )
