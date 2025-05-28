from django.urls import path
from . import views

urlpatterns = [
    path('metadata/', views.metadata_form_view, name='metadata_form'),
    path('metadata/yml-preview/', views.get_yml_preview, name='yml_preview'),
    path('metadata/download/', views.download_yml, name='download_yml'),
]