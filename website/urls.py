# website/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home2, name='home2'),
    path('articles/', views.articles, name='articles'),
    path('services/', views.services, name='services'),
    path('service_analysis/', views.service_analysis, name='service_analysis'),
    path('service_dev_tool/', views.service_dev_tool, name='service_dev_tool'),
    path('service_data_management/', views.service_data_management, name='service_data_management'),
    #path('case-studies/', views.case_studies, name='case_studies'),
    path('contact/', views.contact, name='contact'),
    path('corpoFinance/', views.corpoFinance, name='corpoFinance'),   
    path('rates_analysis/',views.rates_analysis, name='rates_analysis'),
    path('meanReversion/',views.meanReversion, name='meanReversion'),
    path('about/', views.about, name='about'),
    path('tool_risk_calculator/', views.tool_risk_calculator, name='tool_risk_calculator'),
    path('article_automation_for_small_business/', views.article_automation_for_small_business, name='article_automation_for_small_business'),
    path('article_ml_for_small_business/', views.article_ml_for_small_business, name='article_ml_for_small_business'),
    path('article_risk_management/', views.article_risk_management, name='article_risk_management'),
]