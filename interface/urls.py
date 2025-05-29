from django.urls import path
from . import views

urlpatterns = [
    path('', views.computing_form_view, name='computing'),
    path('yml-preview/', views.get_yml_preview, name='yml_preview'),
    path('download/', views.download_yml, name='download_yml'),
]