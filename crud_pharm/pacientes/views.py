from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, "pacientes/index.html")

def section(request):
    
    return render(request, "pacientes/index.html")
