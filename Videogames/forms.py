from django import forms
from django.forms import TextInput, ModelForm
from django.core import validators
from Videogames.models import Videojuego

class FormularioVideoJuego(forms.Form):
    CATEGORIAS = (
      ("Shooter", 'Shooter'),
      ("RPG", 'RPG'),
      ("Competitivo", 'Competitivo'),
      ("Carreras", 'Carreras'),
      ("Terror", 'Terror'),
      ("Survival", 'Survival'))
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
    categoria = forms.ChoiceField(choices=CATEGORIAS)

    precio = forms.FloatField()

    espacio_en_disco = forms.IntegerField(
        validators=[
            validators.MinValueValidator(1, 'el valor debe ser mayor a 1'),
            validators.MaxValueValidator(300, 'El valor tiene que ser menor que 300')
        ]
    )

    fecha_alta = forms.DateField(
        label='Alta del videojuego',
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder' : 'Introducir una fecha de alta '}
        )
    )
    
class FomularioBusqueda(forms.Form):
    titulo = forms.CharField(
        max_length=50, 
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder' : 'Buscar '}
        )
    )

class RichFieldForm(ModelForm):
    class Meta: 
        model = Videojuego
        fields = ['cuerpo']


class PostearImagen(forms.ModelForm):

    class Meta:
        model = Videojuego
        fields = ['titulo', 'categoria', 'precio', 'espacio_en_disco', 'fecha_alta', 'portada', 'cuerpo']
