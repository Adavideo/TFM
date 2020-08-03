from django.shortcuts import render
from topics_identifier.models import Document
from .models import Thread

def timeline_view(request):
    template = "timeline.html"
    all_documents = Document.objects.all().order_by("date")
    context = { "documents_list": all_documents}
    return render(request, template, context)

def threads_list_view(request):
    template = "threads_list.html"
    all_threads = Thread.objects.all()
    context = { "threads_list": all_threads}
    return render(request, template, context)

def thread_view(request, thread_id):
    template = "thread.html"
    thread = Thread.objects.get(id=thread_id)
    context = { "thread": thread }
    return render(request, template, context)
