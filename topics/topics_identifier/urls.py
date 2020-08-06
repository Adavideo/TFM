from django.urls import path
from . import views

urlpatterns = [
    path('generate_tree', views.generate_tree_view, name='generate_tree'),
    path('trees_index', views.trees_index_view, name='trees_index'),
    path('tree/<tree_id>', views.tree_view, name='tree'),
    path('cluster/<cluster_id>', views.cluster_view, name='cluster'),
    path('cluster_topic/<topic>', views.cluster_topic_view, name='cluster_topic'),
]
