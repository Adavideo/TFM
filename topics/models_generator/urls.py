from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_model_view, name='generate_models')
]
