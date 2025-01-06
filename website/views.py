# website/views.py
from django.shortcuts import render
#from .models import CaseStudy

def home2(request):
    return render(request, 'home2.html')

def about(request):
    return render(request, 'aPropos.html')

def services(request):
    return render(request, 'services.html')

def service_analysis(request):
    return render(request, 'service_analysis.html')

def service_dev_tool(request):
    return render(request, 'service_dev_tool.html')

def service_data_management(request):
    return render(request, 'service_data_management.html')

def article_corpo_finance(request):
    return render(request, 'corpoFinance.html')

def contact(request):
    return render(request, 'contact.html')

def rates_analysis(request):
    return render(request, 'ratesAnalysis.html')

def article_mean_reversion(request):
    return render(request, 'meanReversion.html')

def tool_risk_calculator(request):
    return render(request, 'riskCalculator.html')