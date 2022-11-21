from webbrowser import get
from django.shortcuts import render, redirect
from Videogames.models import Videojuego
from Videogames.forms import FormularioVideoJuego, FomularioBusqueda, RichFieldForm, PostearImagen
from datetime import datetime
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import re

def index(request): 
    return render(request, 'layouts/index.html', {'title' : 'inicio'})

def about(request):
    return render(request, 'layouts/about.html')

def ver_catalogo(request): 
    cant_registros = Videojuego.objects.all().count()
    formulario = FomularioBusqueda()
    titulo = request.GET.get('titulo', None)
    if titulo: 
        videojuego = Videojuego.objects.filter(titulo__icontains = titulo)
    else: 
        videojuego = Videojuego.objects.all()    
    return render(request, 'layouts/ver_catalogo.html', {'juego' : videojuego, 'cantidad' : cant_registros,  'form' : formulario})

@login_required
def registrar_videojuego(request):
    if request.method == "POST":  
        # Instancias de los dos formularios para adaptar el RichText a una vista que no está basada en clase.     
        formulario = FormularioVideoJuego(request.POST, request.FILES)      
        formtext = RichFieldForm(request.POST)  

        if formtext.is_valid():
            text_data = formtext.cleaned_data
        else: 
            text_data = 'Error al ingresar datos'

        if formulario.is_valid():
            data = formulario.cleaned_data
            if not data['fecha_alta']:
                fecha_alta = datetime.now()
            else: 
                fecha_alta = data['fecha_alta']
            if data['portada'] is not None:
                imagen = data['portada']
            else: 
                imagen = data['portada']
            
            videojuego = Videojuego(
                titulo = data['titulo']
                ,categoria = data['categoria']
                ,precio = data['precio']
                ,espacio_en_disco = data['espacio_en_disco']
                ,fecha_alta = fecha_alta
                ,autor = request.user
                ,cuerpo = text_data
                ,portada = imagen
            )
            videojuego.save()
            return redirect('catalogo')
        else:
            return render(request, 'layouts/registrar_videojuego.html', {'formulario' : formulario})
    formulario = FormularioVideoJuego()
    return render(request, 'layouts/registrar_videojuego.html', {'formulario' : formulario, 'form' : RichFieldForm()})

def ver_detalles(request, id): 

    # Hace una limpieza de caracteres html si hubo descricpción de texto enriquecido
    videojuego = Videojuego.objects.filter(id = id).values()
    texto = videojuego[0]['cuerpo']
    clean = re.compile('<.*?>')
    limpiar_texto = lambda texto: re.sub(clean, '', texto) if len(texto) > 0 else False 
    if texto is None:
        texto = "Sin descripción"
    else: 
        if limpiar_texto:
            texto = limpiar_texto(texto).replace("&nbsp;", " ")            
            texto_limpio = texto.replace('{', "").replace("}", " ").replace("cuerpo"," ").replace(":"," ").replace("'", " ")
            return render(request, 'layouts/detalles.html', {'juego' : videojuego, 'cleaned_text' : texto_limpio, 'sin_descripcion' : texto})
       

    return render(request, 'layouts/detalles.html', {'juego' : videojuego, 'sin_descripcion' : texto})


class BorrarVideojuego(LoginRequiredMixin, DeleteView): 
    model = Videojuego
    success_url = '/videojuegos/catalogo'
    template_name = 'layouts/borrar_videojuego.html'

class EditarVideojuego(LoginRequiredMixin, UpdateView):  
    model = Videojuego
    form_class = PostearImagen
    template_name = "layouts/editar_videojuego.html"
    success_url =  '/videojuegos/catalogo'
