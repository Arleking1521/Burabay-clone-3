from django.urls import path
from . import views

urlpatterns = [
    path('', views.lek, name = 'LEK-list'),
    path('<int:fid>/', views.file_detail, name = 'Lek-doc-detils'),
]