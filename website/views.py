# website/views.py
from django.shortcuts import render
#from .models import CaseStudy

def home2(request):
    return render(request, 'home2.html')

def services(request):
    return render(request, 'services.html')

def corpoFinance(request):
    return render(request, 'corpoFinance.html')

def contact(request):
    return render(request, 'contact.html')

def ratesAnalysis(request):
    return render(request, 'ratesAnalysis.html')

def meanReversion(request):
    return render(request, 'meanReversion.html')