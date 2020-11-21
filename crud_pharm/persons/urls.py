from django.urls import path
from . import views
from . import class_views

app_name = "persons"

urlpatterns = [
    path("",views.index,name="index"),
    path("viewPersons/",class_views.PersonsView.as_view(),name="viewPersons"),
    path("addPersons/",class_views.PersonsCreate.as_view(),name="addPersons"),
    path("editPersons/<int:pk>",class_views.PersonsUpdate.as_view(),name="editPersons"),
    path("deletePersons/<int:pk>",class_views.PersonsDelete.as_view(),name="deletePersons"),
]