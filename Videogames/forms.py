from attr import attr
from django import forms
from django.forms import TextInput
from django.core import validators
from pyparsing import Regex
from Videogames.models import Videojuego

class FormularioVideoJuego(forms.Form):
    titulo = forms.CharField(
        label = "Titulo",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Título del videojuego '
            }
        ),
        validators=[
            validators.MinLengthValidator(2, 'El titulo es demasiado corto.')
        ]
    )
    categoria = forms.CharField(
        label = "Categoría",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder' : 'Categoría del videojuego '}
        ),
        validators=[
            validators.MinLengthValidator(3, 'El nmbre de la categoría es demasiado corto. ')
        ]
    )
    precio = forms.FloatField()

    espacio_en_disco = forms.IntegerField(
        validators=[
            validators.MinValueValidator(1, 'el valor debe ser mayor a 1'),
            validators.MaxValueValidator(300, 'El valor tiene que ser menor que 300')
        ]
    )

    fecha_alta = forms.DateField(
        label='Alta del videojuego',
        widget=forms.TextInput(
            attrs={'placeholder' : 'Tamaño del videojuego '}
        )
    )

class FomularioBusqueda(forms.Form):
    titulo = forms.CharField(
        max_length=50, 
        required=False
    )

