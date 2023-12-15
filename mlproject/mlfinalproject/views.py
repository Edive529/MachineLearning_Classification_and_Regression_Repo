from django.shortcuts import render, redirect
from django.http import JsonResponse
import pandas as pd
from .models import classificationTable, regressionTable
import joblib
import logging 
from .forms import CSVImportForm 
import csv
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pickle import load 
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.template.loader import render_to_string
import plotly.express as px

def index(request):
    return render(request, 'index.html')

def classification(request):
    return render(request, 'classification.html')

def classification_pred(request):
    if request.POST.get('action') == 'post':
        try:
            # Receive data from client and perform input validation
            age = float(request.POST['age'])
            gender = float(request.POST['gender'])
            impulse = float(request.POST['impulse'])
            pressurehigh = float(request.POST['pressurehigh'])
            pressurelow = float(request.POST['pressurelow'])
            glucose = float(request.POST['glucose'])
            kcm = float(request.POST['kcm'])
            troponin = float(request.POST['troponin'])
 
            model = joblib.load("cart_model.pkl")

            lis = []
            lis.append(age)
            lis.append(gender) 
            lis.append(impulse)
            lis.append(pressurehigh) 
            lis.append(pressurelow)
            lis.append(glucose) 
            lis.append(kcm)
            lis.append(troponin) 

            print(lis)

            result = model.predict([lis])
 
            classification = result[0] 
            #log test
            if classification == 1:
                print("The person's heart is problematic")
            else:
                print("The person's heart is not problematic") 

            classificationTable.objects.create(age=age, gender=gender, impulse=impulse,
                                   pressurehigh=pressurehigh, pressurelow=pressurelow, glucose=glucose,
                                   kcm=kcm, troponin=troponin, classification=classification)
 
            return JsonResponse({'result': classification, 'age': age,
                                 'gender': gender, 'impulse': impulse, 'pressurehigh': pressurehigh,
                                 'pressurelow': pressurelow, 'glucose': glucose, 'kcm': kcm,
                                 'troponin': troponin}, safe=False)


        except Exception as e:
            # Log the error
            logging.error(str(e))
            return JsonResponse({'error': str(e)}, status=500)
 
    return JsonResponse({'error': 'Invalid action'}, status=400)

def reg_pred(request):
    if request.POST.get('action') == 'post':
        try:
            # Load scaler
            with open('scaler.pkl', 'rb') as file:
                scaler = load(file)

            # Receive data from client and perform input validation
            carat = float(request.POST['carat'])
            cut = float(request.POST['cut'])
            color = float(request.POST['color'])
            clarity = float(request.POST['clarity'])
            depth = float(request.POST['depth'])
            table = float(request.POST['table'])
            rx = float(request.POST['rx'])
            ry = float(request.POST['ry'])
            rz = float(request.POST['rz'])

            # Perform feature scaling
            features = scaler.transform([[carat, cut, color, clarity, depth, table, rx, ry, rz]])
            
            # Load model
            with open('RandomForestRegressor_n=150.pkl', 'rb') as file:
                random_forest_regressor = load(file)

            # Make prediction
            price = random_forest_regressor.predict(features).tolist()  # Convert to Python list
            print(price[0])
            lis = []
            lis.append(carat)
            lis.append(cut) 
            lis.append(color)
            lis.append(clarity) 
            lis.append(depth)
            lis.append(table)   

            print(lis)
            # Save to database
            regressionTable.objects.create(carat=carat, cut=cut, color=color,
                                           clarity=clarity, depth=depth, table=table,
                                           x=rx, y=ry, z=rz)

            return JsonResponse({'result': price, 'carat': carat,
                                 'cut': cut, 'color': color, 'clarity': clarity,
                                 'depth': depth, 'table': table, 'rx': rx,
                                 'ry': ry, 'rz': rz}, safe=False)

        except Exception as e:
            # Log the error
            logging.error(str(e))
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid action'}, status=400)

def class_results(request):
    # Submit prediction and show all
    data = {"dataset": classificationTable.objects.all()}
    return render(request, "class_results.html", data)

def mlfinalproject(request):
    return render(request, 'classification.html')
  
def class_viz(request):
    return render(request, 'class_viz.html')


# Create your views here.

#import db

def import_csv(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                regressionTable.objects.create(
                    carat=row['carat'],
                    cut=row['cut'],
                    color=row['color'],
                    clarity=row['clarity'],
                    depth=row['depth'],
                    table=row['table'],
                    x=row['x'],
                    y=row['y'],
                    z=row['z'] 
                )

            return redirect('class_viz')   
    else:
        form = CSVImportForm()

    return render(request, 'import.html', {'form': form})

# views.py
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#pagination
def class_results(request):
    all_data = classificationTable.objects.all()

    # Number of items per page
    items_per_page = 10
    paginator = Paginator(all_data, items_per_page)

    page = request.GET.get('page')
    try:
        dataset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        dataset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page of results.
        dataset = paginator.page(paginator.num_pages)

    return render(request, 'class_results.html', {'dataset': dataset})
 
 

