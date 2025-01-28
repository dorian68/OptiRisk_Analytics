# website/views.py
from django.shortcuts import render
#from .models import CaseStudy
from django.http import JsonResponse
from django.http import HttpResponse
from .models import UploadedFile
from django.shortcuts import redirect
from .forms import UploadedFileForm
from .models import UploadedFile
import pandas as pd
import numpy as np
import json
import os
from website.utils.cls_ExcelToHTML import ExcelToHTML

def upload_file(request):
    data = None  # Pour stocker les données traitées

    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()  # Enregistre le fichier en base
            file_path = uploaded_file.file.path  # Récupère le chemin du fichier

            # Charger le fichier dans un DataFrame pandas
            try:
                if file_path.endswith('.csv'):
                    data = pd.read_csv(file_path)
                elif file_path.endswith(('.xls', '.xlsx')):
                    data = pd.read_excel(file_path)

                # Convertir en HTML pour affichage
                data_html = data.head(10).to_html(classes="table table-striped")

                return render(request, 'report.html', {'data': data_html})

            except Exception as e:
                return render(request, 'upload.html', {'form': form, 'error': str(e)})

    else:
        form = UploadedFileForm()

    return render(request, 'upload.html', {'form': form})

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

from django.shortcuts import render, redirect, get_object_or_404
from .forms import UploadedFileForm
from .models import UploadedFile

def tool_risk_calculator(request):
    form = UploadedFileForm()
    
    if request.method == "POST":
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            return redirect("process_file", file_id=uploaded_file.id)  # Redirection après upload
    
    return render(request, "riskCalculator.html", {"form": form})

def process_file(request, file_id):
    uploaded_file = get_object_or_404(UploadedFile, id=file_id)
    file_path = uploaded_file.file.path

    # Détection automatique du format
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith((".xls", ".xlsx")):
            df = pd.read_excel(file_path)
        else:
            return render(request, "error.html", {"message": "Format de fichier non pris en charge."})

        # Vérification si le DataFrame est vide
        if df.empty:
            print("df is empty")
            return render(request, "error.html", {"message": "Le fichier est vide ou mal formaté."})
        
        html_table_perso = ""
        dev = True

        # Create Values

        # Supposons que df existe déjà
        n = len(df)  # Taille du DataFrame

        # Paramètres du mouvement brownien
        mu = 150      # Drift moyen (peut être modifié)
        sigma = 1    # Volatilité
        dt = 1       # Pas de temps (1 par défaut)

        # Génération du mouvement brownien
        brownian_motion = np.cumsum(np.random.normal(mu * dt, sigma * np.sqrt(dt), n))

        # Ajout au DataFrame sous une nouvelle colonne
        df["values"] = brownian_motion

        # Shrink our dataframe
        df = df.head(5)

        df_input = ExcelToHTML(df)

        # work on user inputs then transforms to html
        html_table_perso = df_input.to_html()

        # Convertir le DataFrame en HTML
        table_html = df.to_html(classes="table table-striped", index=False)

        # Choisir une colonne à afficher (ex: la première colonne comme labels)
        labels = df.iloc[:, 0].astype(str).tolist()
        values = df["values"].tolist() # Deuxième colonne pour les valeurs

        # open excel report as html
        with open(r"C:\Users\Do\Mail\~XLRange.htm","r") as file:
            df_excel_tab = file.read()



        # Convertir les données en JSON pour JavaScript
        context = {
            "table_html": html_table_perso,
            #"table_html": df_excel_tab,
            #"table_html": df.to_html(classes="table table-striped"),
            "labels_json": json.dumps(labels),  # Convertir en JSON
            "values_json": json.dumps(values),  # Convertir en JSON
        }
        return render(request, "report.html", context)

    except Exception as e:
        return render(request, "error.html", {"message": f"Erreur lors du traitement du fichier : {e}"})

def article_automation_for_small_business(request):
    return render(request, 'article_automation_for_small_business.html')

def article_ml_for_small_business(request):
    return render(request, 'article_ml_for_small_business.html')

def article_risk_management(request):
    return render(request, 'article_risk_management.html')

def article_automation_email_sending(request):
    return render(request, 'article_automation_email_sending.html')

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


