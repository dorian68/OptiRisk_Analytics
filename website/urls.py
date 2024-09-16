# website/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    #path('case-studies/', views.case_studies, name='case_studies'),
    path('contact/', views.contact, name='contact'),
]
