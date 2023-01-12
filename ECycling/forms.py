from django import forms    

class ClienteForm (forms.Form):
    cod_cliente=forms.IntegerField (required=True)
    nombre=forms.CharField(max_length=100)
    apellido=forms.CharField (max_length=100,)
    direccion=forms.CharField(max_length=100)
    localidad=forms.CharField(max_length=100)
    cp=forms.IntegerField()
    telefono=forms.CharField(max_length=100)
    email=forms.CharField(max_length=100)

class IndumentariaForm (forms.Form):
    cod_indumentaria=forms.IntegerField ()
    tipo=forms.CharField(max_length=100) 
    genero=forms.CharField(max_length=100)
    nombre=forms.CharField(max_length=100)
    stock=forms.IntegerField ()
    precio=forms.FloatField () 

class BicicletaForm (forms.Form):
    tipo=forms.CharField(max_length=50)
    nombre=forms.CharField(max_length=60) 
    rodado=forms.IntegerField ()
    marca=forms.CharField(max_length=50)
    precio=forms.FloatField () 