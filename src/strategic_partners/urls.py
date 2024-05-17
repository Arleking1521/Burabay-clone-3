from django.urls import path
from . import views

urlpatterns = [
    path('', views.strategicPartners, name = 'strategic_partners'),
]