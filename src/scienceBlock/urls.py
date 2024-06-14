from django.urls import path
from . import views

urlpatterns = [
    path('', views.scienceDev, name = 'science'),
    path('scientific-and-technical-council', views.scienceSovet, name = 'scienceSovet'),
    path('plans', views.sciencePlans, name = 'plans'),
    path('achievments', views.scienceInfo, name = 'science_achievments'),
]