from django.urls import path
from . import views

urlpatterns = [
    # path('', views.scienceInfo, name = 'science_block'),
    path('', views.science, name = 'science'),
    path('scientific-and-technical-council', views.scienceSovet, name = 'scienceSovet'),
    path('plans', views.sciencePlans, name = 'plans'),
]