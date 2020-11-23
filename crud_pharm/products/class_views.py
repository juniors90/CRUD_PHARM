from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import ProductsForm
from .models import Products

class ProductsView(ListView):
    model = Products
    template_name = 'products_list.html'

class ProductsCreate(CreateView):
    model = Products
    form_class = ProductsForm
    template_name = 'products/addProducts.html'
    success_url = reverse_lazy('products:viewProducts')

class ProductsUpdate(UpdateView):
    model = Products
    form_class = ProductsForm
    template_name = 'products/addProducts.html'
    success_url = reverse_lazy('products:viewProducts')

class ProductsDelete(DeleteView):
    model = Products
    template_name = 'products/verif.html'
    success_url = reverse_lazy('products:viewProducts')