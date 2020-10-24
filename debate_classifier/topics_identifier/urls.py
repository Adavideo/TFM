from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='topics_identifier'),
    path('generate_tree', views.generate_tree_view, name='generate_tree'),
    path('trees_index', views.trees_index_view, name='trees_index'),
    path('tree/<tree_id>', views.tree_view, name='tree'),
    path('cluster/<cluster_id>', views.cluster_view, name='cluster'),
    path('topics_index', views.topics_index_view, name='topics_index'),
    path('topic/<topic_id>', views.topic_view, name='topic'),
    path('topic_clusters/<topic_id>', views.topic_clusters_view, name='topic_clusters'),
    path('label_documents/<topic_id>', views.label_documents_view, name='label_documents'),
    path('assign_topic_to_clusters/', views.assign_topic_to_clusters_view, name='assign_topic_to_clusters'),
    path('assign_topic_from_file/', views.assign_topic_from_file_view, name='assign_topic_from_file'),
]
