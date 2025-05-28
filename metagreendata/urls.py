"""
URL configuration for metagreendata project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from interface.views import index, computing_form_view, work_in_progress, get_yml_preview, download_yml

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('computing/', computing_form_view, name='computing'),
    path('work-in-progress/<str:form_type>/', work_in_progress, name='work_in_progress'),
    path('computing/yml-preview/', get_yml_preview, name='yml_preview'),
    path('computing/download/', download_yml, name='download_yml'),
]
