
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from .models import Cliente, Vehiculo, Credito
from .forms import ClienteForm, VehiculoForm, CreditoForm, SearchForm


def index(request):
    return render(request, 'index.html')

def mostrardatos(req):
    clientes = Cliente.objects.all()
    vehiculos = Vehiculo.objects.all()
    return render(req,'mostrardatos.html',{'clientes':clientes,'vehiculos':vehiculos,})

def add_cliente(req):
    if req.method == 'POST':
        form = ClienteForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form = ClienteForm()
    return render(req, 'add_cliente.html', {'form': form})

def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html',{} )
    else:
        form = VehiculoForm()
    return render(request, 'add_vehiculo.html', {'form': form})

def add_credito(request):
    if request.method == 'POST':
        form = CreditoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form = CreditoForm()
    return render(request, 'add_credito.html', {'form': form})

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Vehiculo.objects.filter(marca__icontains=query) | Vehiculo.objects.filter(modelo__icontains=query)
            return render(request, 'search_results.html', {'results': results, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})
