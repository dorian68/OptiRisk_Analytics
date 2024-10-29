# website/views.py
from django.shortcuts import render
#from .models import CaseStudy

def home2(request):
    return render(request, 'home2.html')

def services(request):
    return render(request, 'services.html')

def article1(request):
    return render(request, 'article1.html')

"""def case_studies(request):
    case_studies = CaseStudy.objects.all()
    return render(request, 'case_studies.html', {'case_studies': case_studies})
"""

def contact(request):
    return render(request, 'contact.html')
