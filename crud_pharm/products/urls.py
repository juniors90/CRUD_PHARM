from django.urls import path
from . import views
from . import class_views

app_name = "products"

urlpatterns = [
    path("",views.index,name="index"),
    path("viewProducts/",class_views.ProductsView.as_view(),name="viewProducts"),
    path("addProducts/",class_views.ProductsCreate.as_view(),name="addProducts"),
    path("editProducts/<int:pk>",class_views.ProductsUpdate.as_view(),name="editProducts"),
    path("deleteProducts/<int:pk>",class_views.ProductsDelete.as_view(),name="deleteProducts"),
]