from django import forms
from django.forms import ModelForm, fields
from .models import Producto
from .models import Vehiculo

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto', 'producto', 'detalles', 'imagen', 'categoria']

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'imagen','servicio','detalle_servicio', 'categoria']