from django.db import models

# Create your models here.
class cliente(models.Model):
    cod_cliente=models.IntegerField (null=False, default=0)
    nombre=models.CharField(max_length=100,null=True)
    apellido=models.CharField (max_length=100,null=True)
    direccion=models.CharField(max_length=100,null=True)
    localidad=models.CharField(max_length=100,null=True)
    cp=models.IntegerField(null=True)
    telefono=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)

class indumentaria(models.Model):
    cod_indumentaria=models.IntegerField (null=False, default=0)
    tipo=models.CharField(max_length=100,null=True) 
    genero=models.CharField(max_length=100,null=True)
    nombre=models.CharField(max_length=100,null=True)
    stock=models.IntegerField (null=False,default=0)
    precio=models.FloatField (null=False,default=0)

class venta(models.Model):
    fecha=models.CharField(max_length=100,null=True) 
    cod_cliente=models.IntegerField (null=False,default=0)
    cod_indumetaria=models.IntegerField (null=False,default=0)
    cantidad=models.IntegerField (null=False,default=0)

class bicicletas(models.Model):
    tipo=models.CharField(max_length=50,null=False)
    nombre=models.CharField(max_length=60,null=False)
    rodado=models.IntegerField(null=False,default=0)
    marca=models.CharField(max_length=50,null=True)
    precio=models.FloatField (null=False,default=0)

