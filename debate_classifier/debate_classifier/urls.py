"""debate classifier URL Configuration

The `urlpatterns` list routes URLs to views.

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('topics_identifier/', include('topics_identifier.urls')),
    path('import_csv/', include('csv_import.urls')),
    path('models_generator/', include('models_generator.urls')),
    path('timeline/', include('timeline.urls')),
    path('arguments/', include('arguments.urls')),
    path('metrics/', include('metrics.urls'))
]
