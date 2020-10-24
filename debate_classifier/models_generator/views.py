from django.shortcuts import render
from .forms import ModelsForm
from .ModelsManager import ModelsManager
from .documents_selector import select_documents


def generate_model_view(request):
    template = "models_generator/generate_model.html"

    if request.method == "GET":
        context = { "form": ModelsForm() }

    if request.method == "POST":
        # Read values from the form
        model_name = request.POST["model_name"]
        document_types = request.POST["document_types"]
        max_num_documents = int(request.POST["max_num_documents"])
        max_level = int(request.POST["max_level"])
        # Generate and store model
        models_manager = ModelsManager(name=model_name)
        documents = select_documents(document_types, max_num_documents)
        filenames = models_manager.generate_and_store_models(documents, max_level)
        # Context for web page
        context = { "model_name": model_name, "filenames": filenames }

    return render(request, template, context)
