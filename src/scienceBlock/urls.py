from django.urls import path
from . import views

urlpatterns = [
    # path('', views.scienceInfo, name = 'science_block'),
    path('', views.science, name = 'science'),
]