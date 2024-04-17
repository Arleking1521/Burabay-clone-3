from django.urls import path
from . import views

urlpatterns = [
    path('', views.ethics_list, name = 'ethicsRegulations'),
    path('download/<int:did>/', views.download_file, name='download_file'),
]