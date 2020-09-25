from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='metrics'),
    path('generate_sample', views.generate_sample_view, name='generate_sample')
]
