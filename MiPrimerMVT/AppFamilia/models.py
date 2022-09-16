from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=60)
    relacion = models.CharField(max_length=60)
    nacimiento = models.DateField()