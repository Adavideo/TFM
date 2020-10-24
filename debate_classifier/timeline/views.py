from django.shortcuts import render
from .models import Thread, Document, Topic
from .threads_manager import check_threads_without_news

def timeline_view(request):
    template = "timeline/timeline_home.html"
    context = { }
    return render(request, template, context)

def threads_list_view(request):
    template = "timeline/threads_list_page.html"
    threads_list = Thread.objects.all()
    context = { "threads_list": threads_list }
    return render(request, template, context)

def topic_threads_view(request, topic_id):
    template = "timeline/threads_list_page.html"
    topic = Topic.objects.get(id=topic_id)
    threads_list = topic.get_threads()
    context = { "threads_list": threads_list, "topic": topic.name }
    return render(request, template, context)

def thread_view(request, thread_id):
    template = "timeline/thread.html"
    thread = Thread.objects.get(id=thread_id)
    news = thread.news()
    comments_list = thread.comments()
    context = { "thread": thread, "news": news, "comments_list": comments_list }
    return render(request, template, context)

def check_threads_view(request):
    template = "timeline/check_threads.html"
    no_news = check_threads_without_news()
    context = { "threads_without_news": no_news, "number": len(no_news) }
    return render(request, template, context)

def topics_list_view(request):
    template = "timeline/topics_list.html"
    topics_list = Topic.objects.all()
    context = { "topics_list": topics_list }
    return render(request, template, context)
