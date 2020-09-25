from django.shortcuts import render
from .forms import GenerateSampleForm
from timeline.models import Topic


def home_view(request):
    template = "metrics/metrics_home.html"
    context = {}
    return render(request, template, context)

def generate_sample_view(request):
    template = "metrics/generate_sample.html"
    if request.method == "GET":
        form = GenerateSampleForm()
        context = { "form": form }
    else:
        filename = request.POST["filename"]
        topic_id = request.POST["topic"]
        topic = Topic.objects.get(id=topic_id)
        context = { "filename": filename, "topic": topic }
    return render(request, template, context)
