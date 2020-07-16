from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('import_files', views.import_files_view, name='import_files'),
    path('generate_dataset', views.generate_dataset_view, name='generate_dataset'),
    path('generate_clusters', views.generate_clusters_level0_view, name='generate_clusters'),
    path('generate_clusters_level1', views.generate_clusters_level1_view, name='generate_clusters_level1'),
    path('clusters', views.clusters_view, name='all_clusters'),
    path('clusters/<dataset_name>', views.clusters_view, name='dataset_clusters'),
    path('clusters_index', views.clusters_index_view, name='clusters_index'),
]
