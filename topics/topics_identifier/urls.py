from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('import_files', views.import_files, name='import_files'),
]
