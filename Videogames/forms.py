from django import forms
from Videogames.models import Videojuego

class FormularioVideoJuego(forms.Form):
    titulo = forms.CharField(max_length=50)
    categoria = forms.CharField(max_length=30)
    precio = forms.FloatField()
    espacio_en_disco = forms.IntegerField()
    fecha_alta = forms.DateField(required=False)

class FomularioBusqueda(forms.Form):
    titulo = forms.CharField(max_length=50, required=False)

