from django.shortcuts import render
from django.http import HttpResponse
from ECycling.models import cliente
from ECycling.models import indumentaria
from ECycling.models import bicicletas
from ECycling.forms import ClienteForm 
from ECycling.forms import IndumentariaForm
from ECycling.forms import BicicletaForm

def crea_clientes(request):
    if request.method=='GET':
        context ={
            'form': ClienteForm()
        }

        return render (request,'Clientes/create_clientes.html',context=context)
    elif request.method=='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente.objects.create(
                cod_cliente=form.cleaned_data['cod_cliente'],
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                direccion=form.cleaned_data['direccion'],
                localidad=form.cleaned_data['localidad'],
                cp=form.cleaned_data['cp'],
                telefono=form.cleaned_data['telefono'],
                email=form.cleaned_data['email'],
                )
            context={
                'message': 'El Clientes ha sido creado'

                }
            return render (request,'Clientes/create_clientes.html',context=context)
        else:
            context ={
                'form_errors': form.errors,
                'form':ClienteForm()
            }
            return render (request,'Clientes/create_clientes.html',context=context)


def crea_indumentaria(request):
    if request.method=='GET':
        context ={
            'form': IndumentariaForm()
        }

        return render (request,'Productos/create_indumentaria.html',context=context)
    elif request.method=='POST':
        form = IndumentariaForm(request.POST)
        if form.is_valid():
            indumentaria.objects.create(
                cod_indumentaria=form.cleaned_data['cod_indumentaria'],
                tipo=form.cleaned_data['tipo'], 
                genero=form.cleaned_data['genero'],
                nombre=form.cleaned_data['nombre'],
                stock=form.cleaned_data['stock'],
                precio=form.cleaned_data['precio'], 
                )
            context={
                'message': 'El Producto ha sido creado'

                }
            return render (request,'Productos/create_indumentaria.html',context=context)
        else:
            context ={
                'form_errors': form.errors,
                'form':IndumentariaForm()
            }
            return render (request,'Productos/create_indumentaria.html',context=context)            

def crea_bicicletas(request):
    if request.method=='GET':
        context ={
            'form': BicicletaForm()
        }

        return render (request,'Productos/create_bicicleta.html',context=context)
    elif request.method=='POST':
        form = BicicletaForm(request.POST)
        if form.is_valid():
            bicicletas.objects.create(
                tipo=form.cleaned_data['tipo'],
                nombre=form.cleaned_data['nombre'], 
                rodado=form.cleaned_data['rodado'],
                marca=form.cleaned_data['marca'],
                precio=form.cleaned_data['precio'], 
                )
            context={
                'message': 'La bicicleta ha sido creada'

                }
            return render (request,'Productos/create_bicicleta.html',context=context)
        else:
            context ={
                'form_errors': form.errors,
                'form':BicicletaForm()
            }
            return render (request,'Productos/create_bicicleta.html',context=context)   
   

def lista_clientes(request):
    print (request.GET)
    if 'search' in request.GET:
        search = request.GET['search']
        clientes = cliente.objects.filter(nombre__contains=search)
    else:
        clientes = cliente.objects.all()
    context={
        'clientes':clientes,
        }
    return render (request, 'Clientes/lista_clientes.html', context=context)

def lista_indumentaria(request):
    print (request.GET)
    if 'search' in request.GET:
        search = request.GET['search']
        indumentarias = indumentaria.objects.filter(nombre__contains=search)
    else:
        indumentarias = indumentaria.objects.all()
    context={
        'indumentarias':indumentarias,
        }
    return render (request, 'Productos/lista_indumentaria.html', context=context)

def lista_bicicleta(request):
    
    if 'search' in request.GET:
        search = request.GET['search']
        bicicletas1 = bicicletas.objects.filter(nombre__contains=search)
    else:
        bicicletas1 = bicicletas.objects.all()
    context={
        'bicicletas':bicicletas1,
        }
    return render (request, 'Productos/lista_bicicletas.html', context=context)

def index(request):
    return render (request, 'index.html', context={})   







