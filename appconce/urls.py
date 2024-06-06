from django.urls import path
from appconce.views import  (
    index,
    add_cliente,
    add_vehiculo,
    add_credito,
    search,
    mostrardatos
)

urlpatterns = [
    path('', index, name='index'),
    path('add_cliente/', add_cliente, name='add_cliente'),
    path('add_vehiculo/',add_vehiculo, name='add_vehiculo'),
    path('add_credito/',add_credito, name='add_credito'),
    path('search/',search, name='search'),
    path('mostrar_vehiculos/',mostrardatos, name='mostrar_vehiculos'),
]