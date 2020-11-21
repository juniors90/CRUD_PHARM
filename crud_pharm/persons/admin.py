from django.contrib import admin
from .models import Persons

# Register your models here.
class PersonsAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email")

admin.site.register(Persons, PersonsAdmin)