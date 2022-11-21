from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Videojuego(models.Model): 

    titulo = models.TextField(max_length = 50)
    categoria = models.TextField(max_length = 20)
    precio = models.FloatField()
    espacio_en_disco = models.IntegerField()
    fecha_alta = models.DateField()
    portada = models.ImageField(upload_to='avatares',null=True, blank=True)
    cuerpo = RichTextField(blank=True, null=True)
    autor = models.TextField(max_length = 50)

    def __str__(self):
        return f'{self.titulo}'
