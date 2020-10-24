from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='arguments'),
    path('generate_topic_tree', views.generate_topic_tree_view, name='generate_topic_tree'),
]
