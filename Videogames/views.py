from django.shortcuts import render, redirect
from Videogames.models import Videojuego
from Videogames.forms import FormularioVideoJuego, FomularioBusqueda
from datetime import datetime


def index(request): 
    return render(request, 'layouts/index.html', {'title' : 'inicio'})


def ver_catalogo(request): 

    cant_registros = Videojuego.objects.all().count()
    formulario = FomularioBusqueda()

    titulo = request.GET.get('titulo', None)
    if titulo: 
        videojuego = Videojuego.objects.filter(titulo__icontains = titulo)
    else: 
        videojuego = Videojuego.objects.all()
    
    return render(request, 'layouts/ver_catalogo.html', {'juego' : videojuego, 'cantidad' : cant_registros,  'form' : formulario})
    


def registrar_videojuego(request):

    if request.method == "POST":
        
        formulario = FormularioVideoJuego(request.POST)
        
        if formulario.is_valid():

            data = formulario.cleaned_data

            if not data['fecha_alta']:
                fecha_alta = datetime.now()
            else: 
                fecha_alta = data['fecha_alta']
                           
            videojuego = Videojuego(

                titulo = data['titulo']
                ,categoria = data['categoria']
                ,precio = data['precio']
                ,espacio_en_disco = data['espacio_en_disco']
                ,fecha_alta = fecha_alta 
            )
            videojuego.save()
            
            return redirect('catalogo')

    formulario = FormularioVideoJuego()  
    return render(request, 'layouts/registrar_videojuego.html', {'formulario' : formulario})
