from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Persons # Importamos el modelo de personsa
from .forms import PersonForm # Importamos el modelo de personsa

# Create your views here.

def index(request):
    return render(request, "persons/index.html")

def viewPersons(request):
    form=Persons.objects.all()
    ctx={
        'persons_form':form
    }
    return render(request, "persons/viewPersons.html", ctx)

def addPersons(request):
    if request.method == 'GET':
        form=PersonForm()
        ctx={
            'form':form
        }
    else:
        form=PersonForm(request.POST)
        ctx={
            'form':form
        }
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("persons:viewPersons"))
    return render(request, "persons/createPersons.html",ctx)


def editPersons(request, id):
    persons_form=Persons.objects.get(pk = id)
    if request.method == 'GET':
        form=PersonForm(instance = persons_form)
        ctx={
            'form':form
        }
    else:
        form=PersonForm(request.POST, instance = persons_form)
        ctx={
            'form':form
        }
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("persons:viewPersons"))
    return render(request, "persons/createPersons.html",ctx)

def deletePersons(request, id):
    persons_form=Persons.objects.get(pk = id)
    persons_form.delete()
    return HttpResponseRedirect(reverse("persons:viewPersons"))
