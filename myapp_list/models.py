from django.db import models

# Create your models here.

class pais(models.Model):
    codigo=models.CharField(max_length=5)
    nombre=models.CharField(max_length=25)
    continente=models.CharField(max_length=20)


class ciudad(models.Model):
    ciudad_pais=models.ForeignKey(pais)
    nombre=models.CharField(max_length=25)
    poblacion=models.IntegerField(default=0)

class lenguaje(models.Model):
    lenguaje_pais=models.ForeignKey(pais)
    lenguaje_nombre=models.CharField(max_length=25)




