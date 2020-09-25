from django.shortcuts import render
from timeline.models import Topic
from .forms import GenerateSampleForm
from .SampleGenerator import SampleGenerator


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
        documents = SampleGenerator(topic, filename).generate_sample()
        context = { "filename": filename, "topic": topic, "documents": documents }
    return render(request, template, context)
