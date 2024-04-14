from django.urls import path
from . import views

urlpatterns = [
    path('', views.accreditation_list, name = 'accreditation'),
    path('<int:pid>/', views.accreditation_detail, name = 'accredit_detail'),
]