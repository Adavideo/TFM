from django.shortcuts import render
from .forms import *
from .csv_importer import process_csv

def index(request):
    template = "topics_identifier/file_upload.html"
    form = ImportCSVForm()
    context = {'form': form }

    if request.method == "POST":
        file = request.FILES['file']
        result = process_csv(file)
        context["result"] = result

    return render(request, template, context)
