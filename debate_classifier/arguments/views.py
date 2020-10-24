from django.shortcuts import render
from timeline.models import Topic, Thread
from .forms import *
from .topic_tree_generator import generate_tree_with_topic_documents


def home_view(request):
    template = "arguments/arguments_home.html"
    threads_ids = [35306, 25664, 26240, 10272, 34325]
    for id in threads_ids:
        thread = Thread.objects.get(id=id)
        print("\n"+str(id)+": "+thread.title)
        print(thread.news().content)
    context = {}
    return render(request, template, context)

def generate_topic_tree_view(request):
    template = "arguments/generate_topic_tree.html"
    if request.method == "GET":
        form = TopicsForm()
        context = { "form": form }
    else:
        topic_id = request.POST["topic"]
        topic = Topic.objects.get(id=topic_id)
        tree_name = request.POST["tree_name"]
        tree = generate_tree_with_topic_documents(topic, tree_name)
        context = { "topic_name": topic.name, "tree":tree }
    return render(request, template, context)
