from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('import_files', views.import_files_view, name='import_files'),
    path('generate_dataset', views.generate_dataset_view, name='generate_dataset'),
    path('cluster_data', views.cluster_data_view, name='cluster_data'),
    path('clusters', views.clusters_view, name='all_clusters'),
    path('clusters/<dataset_name>', views.clusters_view, name='dataset_clusters'),
]
