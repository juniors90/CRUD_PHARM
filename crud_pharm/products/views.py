from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Products # Importamos el modelo de personsa

# Create your views here.

def index(request):
    form=Products.objects.all()
    ctx={
        'form':form
    }
    return render(request, "products/index.html", ctx)