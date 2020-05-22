from django.shortcuts import render
from .forms import *
from .csv_importer import process_csv
from .data_importer import load_and_store_dataset

def index(request):
    template = "topics_identifier/home.html"
    context = {}
    return render(request, template, context)

def import_files(request):
    template = "topics_identifier/file_upload.html"
    form = ImportCSVForm()
    context = {'form': form }

    if request.method == "POST":
        file = request.FILES['file']
        context["result"] = process_csv(file)

    return render(request, template, context)

def generate_dataset(request):
    template = "topics_identifier/generate_dataset.html"
    dataset = load_and_store_dataset()
    context = { "result": dataset }
    return render(request, template, context)
