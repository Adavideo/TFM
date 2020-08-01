from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('import_files', views.import_files_view, name='import_files'),
    path('generate_tree', views.generate_tree_view, name='generate_tree'),
    path('trees_index', views.trees_index_view, name='trees_index'),
    path('tree/<tree_id>', views.tree_view, name='tree'),
    path('cluster/<cluster_id>', views.cluster_view, name='cluster'),
]
