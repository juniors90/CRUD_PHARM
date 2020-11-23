from django import forms
from .models import Products # Importamos el modelo de personsa

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'