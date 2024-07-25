from django.urls import path
from . import views

urlpatterns = [
    path('', views.scienceDev, name = 'science'),
    path('scientific-and-technical-council', views.scienceSovet, name = 'scienceSovet'),
    path('plans', views.sciencePlans, name = 'plans'),
    path('achievments', views.scienceInfo, name = 'science_achievments'),
    path('creation/<int:fid>/', views.creation_details, name = 'creation_details'),
    path('regulation/<int:fid>/', views.regulation_details, name = 'regulation_details'),
    path('plan/<int:fid>/', views.plan_detail, name = 'plan_details'),
]