from django.db import models

# Create your models here.
class Products(models.Model):
    id_product = models.AutoField(primary_key=True)
    name_product = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    stock = models.IntegerField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.name_product