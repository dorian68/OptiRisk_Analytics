# website/views.py
from django.shortcuts import render
#from .models import CaseStudy
from django.http import JsonResponse

def home2(request):
    return render(request, 'home2.html')

def about(request):
    return render(request, 'aPropos.html')

def articles(request):
    return render(request,'articles.html')

def services(request):
    return render(request, 'services.html')

def service_analysis(request):
    return render(request, 'service_analysis.html')

def service_dev_tool(request):
    return render(request, 'service_dev_tool.html')

def service_data_management(request):
    return render(request, 'service_data_management.html')

def corpoFinance(request):
    return render(request, 'corpoFinance.html')

def contact(request):
    return render(request, 'contact.html')

def rates_analysis(request):
    return render(request, 'ratesAnalysis.html')

def meanReversion(request):
    return render(request, 'meanReversion.html')

def tool_risk_calculator(request):
    return render(request, 'riskCalculator.html')

def article_automation_for_small_business(request):
    return render(request, 'article_automation_for_small_business.html')

def article_ml_for_small_business(request):
    return render(request, 'article_ml_for_small_business.html')

def article_risk_management(request):
    return render(request, 'article_risk_management.html')

def chart_data(request):
    # Exemple de données pour la courbe
    data = {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "datasets": [
            {
                "label": "Ventes",
                "data": [12, 19, 3, 5, 2, 3],
                "borderColor": "rgba(75, 192, 192, 1)",
                "backgroundColor": "rgba(75, 192, 192, 0.2)",
                "fill": True
            }
        ]
    }
    return JsonResponse(data)

def chart_view(request):
    return render(request, "chart.html")


