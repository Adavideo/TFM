from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeline_view, name='timeline'),
    path('threads', views.threads_list_view, name='threads_list'),
    path('thread/<thread_id>', views.thread_view, name='thread'),
]
