from django.urls import path
from . import views

urlpatterns = [
    path('', views.import_files_view, name='import_files'),
]
