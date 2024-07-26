from django.urls import path
from . import views

urlpatterns = [
    path('', views.lek, name = 'LEK-list'),
    path('creation/<int:fid>/', views.creation_details, name = 'lek_creation_details'),
    path('regulation/<int:fid>/', views.regulation_details, name = 'lek_regulation_details'),
    path('<int:fid>/', views.file_detail, name = 'Lek-doc-detils'),
    path('plan/<int:fid>/', views.plan_detail, name = 'lek_plan_details'),
]