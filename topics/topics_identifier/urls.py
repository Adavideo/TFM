from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='topics_identifier'),
    path('generate_model', views.generate_model_view, name='generate_model'),
    path('generate_tree', views.generate_tree_view, name='generate_tree'),
    path('trees_index', views.trees_index_view, name='trees_index'),
    path('tree/<tree_id>', views.tree_view, name='tree'),
    path('cluster/<cluster_id>', views.cluster_view, name='cluster'),
    path('assign_topic_from_file/', views.assign_topic_from_file_view, name='assign_topic_from_file'),
    path('cluster_topic/', views.cluster_topic_view, name='cluster_topic'),
]
