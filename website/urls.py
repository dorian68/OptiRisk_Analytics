# website/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home2, name='home2'),
    path('services/', views.services, name='services'),
    path('service_analysis/', views.service_analysis, name='service_analysis'),
    path('service_dev_tool/', views.service_dev_tool, name='service_dev_tool'),
    path('service_data_management/', views.service_data_management, name='service_data_management'),
    #path('case-studies/', views.case_studies, name='case_studies'),
    path('contact/', views.contact, name='contact'),
    path('article_corpo_finance/', views.article_corpo_finance, name='article_corpo_finance'),   
    path('rates_analysis/',views.rates_analysis, name='rates_analysis'),
    path('article_mean_reversion/',views.article_mean_reversion, name='article_mean_reversion'),
    path('about/', views.about, name='about'),
    path('tool_risk_calculator/', views.tool_risk_calculator, name='tool_risk_calculator'),
]