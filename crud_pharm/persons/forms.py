from django import forms
from .models import Persons # Importamos el modelo de personsa

class PersonForm(forms.ModelForm):
    class Meta:
        model = Persons
        fields = ('id_person','first_name','last_name','email',)