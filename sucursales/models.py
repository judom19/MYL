from django.db import models
from django.forms import CharField, ImageField

# Create your models here.
class Sucursales(models.Model):
    nombre_sucursal = models.CharField(max_length=50)
    horario_sucursal = models.CharField(max_length=50)
    direccion_sucursal = models.CharField(max_length=50)
    numero_telefono = models.CharField(max_length=20)
    imagen_sucursal = ImageField()
    class Meta:
        verbose_name = 'Susursal'
        verbose_name_plural = 'Sucursales'
    def __str__(self):
        return self.nombre_sucursal
        




