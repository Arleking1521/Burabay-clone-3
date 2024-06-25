from django.urls import path
from . import views

urlpatterns = [
    path('', views.compServList, name = 'compServ'),
    path('<int:fid>/', views.file_detail, name = 'compServDetails'),
]