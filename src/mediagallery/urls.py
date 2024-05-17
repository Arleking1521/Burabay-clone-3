from django.urls import path
from . import views

urlpatterns = [
    path('', views.MediagalleryServices, name = 'mediagallery'),
    # path('download/<int:did>/', views.download_file, name='download_file'),
]