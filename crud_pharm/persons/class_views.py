from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import  reverse_lazy
from .forms import PersonForm
from .models import Persons


class PersonsView(ListView):
    model = Persons
    template_name = 'persons_list.html'

class PersonsCreate(CreateView):
    model = Persons
    form_class = PersonForm
    template_name = 'persons/addPersons.html'
    success_url = reverse_lazy('persons:viewPersons')

class PersonsUpdate(UpdateView):
    model = Persons
    form_class = PersonForm
    template_name = 'persons/addPersons.html'
    success_url = reverse_lazy('persons:viewPersons')

class PersonsDelete(DeleteView):
    model = Persons
    template_name = 'persons/verif.html'
    success_url = reverse_lazy('persons:viewPersons')