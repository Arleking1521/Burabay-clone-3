from django.urls import path
from . import views


urlpatterns = [
    path('', views.ads, name = 'ads'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]