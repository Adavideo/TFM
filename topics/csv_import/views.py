from django.shortcuts import render
from .forms import ImportCSVForm
from .csv_importer import process_csv

def import_files_view(request):
    template = "csv_import/import_csv.html"
    form = ImportCSVForm()
    context = {'form': form }
    if request.method == "POST":
        file = request.FILES['file']
        registers = process_csv(file)
        context["registers"] = registers[:100]
        context["num_registers"] = len(registers)
    return render(request, template, context)
