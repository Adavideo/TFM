from django.shortcuts import render
from .models import Thread, Document

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
    comments_list = thread.comments()
    context = { "thread": thread, "comments_list": comments_list }
    return render(request, template, context)
