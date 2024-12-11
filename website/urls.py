# website/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home2, name='home2'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('serviceFirst/', views.serviceFirst, name='serviceFirst'),
    path('serviceSecond/', views.serviceSecond, name='serviceSecond'),
    path('serviceThird/', views.serviceThird, name='serviceThird'),
    #path('case-studies/', views.case_studies, name='case_studies'),
    path('contact/', views.contact, name='contact'),
    path('corpoFinance/', views.corpoFinance, name='corpoFinance'),   
    path('ratesAnalysis/',views.ratesAnalysis, name='ratesAnalysis'),
    path('meanReversion/',views.meanReversion, name='meanReversion'),
]
