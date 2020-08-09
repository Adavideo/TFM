from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeline_view, name='timeline'),
    path('threads/', views.threads_list_view, name='threads_list'),
    path('thread/<thread_id>', views.thread_view, name='thread'),
    path('check_threads', views.check_threads_view, name='check_threads'),
    path('topics', views.topics_list_view, name='topics_list'),
    path('topic_threads/<topic_id>', views.topic_threads_view, name='topic_threads'),
]
