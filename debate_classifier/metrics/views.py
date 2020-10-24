from django.shortcuts import render
from timeline.models import Topic
from .models import TopicAnnotation
from .forms import GenerateSampleForm, TopicClassificationForm
from .SampleGenerator import SampleGenerator
from .RelevanceCalculator import RelevanceCalculator
from .inter_annotator_agreement import calculate_inter_annotator_agreement


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

def topic_classification_metrics_view(request):
    template = "metrics/topic_classification.html"
    if request.method == "GET":
        form = TopicClassificationForm()
        context = { "form": form }
    else:
        topic = Topic.objects.get(id=request.POST["topic"])
        context = { "topic": topic.name }
        annotations = TopicAnnotation.objects.filter(topic=topic)
        if annotations:
            context["agreement_score"] = calculate_inter_annotator_agreement(annotations)
            model_name = request.POST["model_name"]
            relevance_calulator = RelevanceCalculator(topic, model_name)
            precision, recall = relevance_calulator.get_relevance_metrics(annotations)
            context["precision"] = precision
            context["recall"] = recall
    return render(request, template, context)
