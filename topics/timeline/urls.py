from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeline_view, name='timeline'),
]
