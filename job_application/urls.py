from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("apply/", views.apply, name="apply"),
    path("details/", views.details, name="details"),
    path("admin/", views.admin, name="admin"),
    
   
   
    # path('job/<int:job_id>/', views.job_details, name='job_details'),
    # path('application/<int:app_id>/', views.application_details, name='application_details'),

]
