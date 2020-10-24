from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='metrics'),
    path('generate_sample', views.generate_sample_view, name='generate_sample'),
    path('topic_classification', views.topic_classification_metrics_view, name='topic_classification_metrics' )
]
