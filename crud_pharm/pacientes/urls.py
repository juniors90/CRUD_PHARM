from django.urls import path
from . import views

app_name = "pacientes"

urlpatterns = [
    path("",views.index,name="index"),
    path("section/",views.section,name="section"),
]