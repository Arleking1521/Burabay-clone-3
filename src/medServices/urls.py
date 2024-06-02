from django.urls import path
from . import views

urlpatterns = [
    path('', views.medicine, name = 'medicine'),
    path('/services', views.medServices, name = 'med-services'),
]