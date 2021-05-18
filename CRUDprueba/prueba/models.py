from typing import Union
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.manager import Manager


class Paises(models.Model):
    id = models.AutoField(primary_key=True)
    Country_name = models.CharField(max_length=100)  

    def __str__(self):
        return self.Country_name

class Categorias(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Ciudades(models.Model):
    id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.city_name 

class Clientes(models.Model):
    id = models.AutoField(primary_key=True) 
    name_client = models.CharField(max_length=100)
    country = models.ForeignKey(Paises, models.DO_NOTHING)
    city = models.ForeignKey(Ciudades,on_delete=models.CASCADE)
    category = models.ForeignKey(Categorias, models.DO_NOTHING)
    user_createc = models.DateField()
    is_active = models.IntegerField(blank=True , null=True)
    Update = models.DateField()
    def __str__(self):
        return self.name_client 