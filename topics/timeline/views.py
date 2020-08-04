from django.shortcuts import render
from .models import Thread, Document
from .threads_manager import check_threads_without_news

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
    news = thread.news()
    comments_list = thread.comments()
    context = { "thread": thread, "news": news, "comments_list": comments_list }
    return render(request, template, context)

def check_threads_view(request):
    template = "check_threads.html"
    no_news = check_threads_without_news()
    context = { "threads_without_news": no_news, "number": len(no_news) }
    return render(request, template, context)
