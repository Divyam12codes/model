from django.http import HttpResponse
from django.shortcuts import render 
import joblib 

def home(request):
    return render(request,"home.html")

def result(request):
    cls=joblib.load('results.csv')
    return render(request,"result.html")

     