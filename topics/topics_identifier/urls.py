from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('import_files', views.import_files_view, name='import_files'),
    path('generate_clusters', views.generate_clusters_level0_view, name='generate_clusters'),
    path('generate_clusters_level1', views.generate_clusters_level1_view, name='generate_clusters_level1'),
    path('clusters_index', views.clusters_index_view, name='clusters_index'),
    path('clusters_tree/<dataset_name>', views.clusters_tree_view, name='clusters_tree'),
    path('cluster/<cluster_id>', views.cluster_view, name='cluster'),
]
