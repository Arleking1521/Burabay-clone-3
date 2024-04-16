from django.urls import path
from . import views

urlpatterns = [
    path('', views.stratDev_list, name = 'srategic-dev'),
    path('download/<int:sid>/', views.download_file, name='download_file'),
]