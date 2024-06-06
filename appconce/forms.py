from django import forms
from .models import Cliente, Vehiculo, Credito

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'anio', 'precio']

class CreditoForm(forms.ModelForm):
    class Meta:
        model = Credito
        fields = ['cliente', 'vehiculo', 'monto', 'aprobado']

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)
