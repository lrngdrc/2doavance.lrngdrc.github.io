from django.db import models

# Create your models here.
class razas(models.Model):
    codigoRazas = models.CharField(max_length=10)
    descripcionRazas = models.CharField(max_length=255)
    estatus = models.BooleanField()