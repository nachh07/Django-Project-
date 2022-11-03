from webbrowser import get
from django.shortcuts import render, redirect
from Videogames.models import Videojuego
from Videogames.forms import FormularioVideoJuego, FomularioBusqueda
from datetime import datetime
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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

@login_required
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

        else:
            return render(request, 'layouts/registrar_videojuego.html', {'formulario' : formulario})

    formulario = FormularioVideoJuego()

    return render(request, 'layouts/registrar_videojuego.html', {'formulario' : formulario})

@login_required
def editar_videojuego(request, id): 
    
    videojuego = Videojuego.objects.get(id=id)

    if request.method == "POST":
        formulario = FormularioVideoJuego(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            videojuego = Videojuego(
                titulo = data['titulo']
                ,categoria = data['categoria']
                ,precio = data['precio']
                ,espacio_en_disco = data['espacio_en_disco']
                ,fecha_alta = data['fecha_alta'] 
            )
            videojuego.save()
            redirect('catalogo')
        else:
            return render(request, 'layouts/editar_videojuego.html', {'formulario' : formulario})

    # hay que ver como hacer para pasarle los campos necesarios
    formulario = FormularioVideoJuego(
        initial={
            'titulo' : videojuego.titulo,
            'categoria' : videojuego.categoria,
            'precio' : videojuego.precio,
            'espacio_en_disco' : videojuego.espacio_en_disco,
            'fecha_alta' : videojuego.fecha_alta
        }
    ) 

    return render(request, 'layouts/editar_videojuego.html', {'formulario' : formulario, 'juego' : videojuego})

@login_required
def borrar_videojuego(request, id): 
    videojuego = Videojuego.objects.get(id=id)
    videojuego.delete()
    return redirect('catalogo')    


class ListarVideojuegos(ListView): 

    model = Videojuego
    template_name = 'layouts/ver_catalogo.html'

class RegistrarVideojuego(LoginRequiredMixin, CreateView): 
    # videojuegos/catalogo/
    model = Videojuego
    success_url = '/videojuegos/'
    template_name = 'layouts/registrar_videojuego.html'
    fields = ['titulo', 'categoria', 'precio', 'espacio_en_disco', 'fecha_alta']

class EditarVideojuego(LoginRequiredMixin, UpdateView):

    model = Videojuego
    success_url = '/videojuegos/'
    template_name = 'layouts/editar_videojuego.html'
    fields = ['titulo', 'categoria', 'precio', 'espacio_en_disco', 'fecha_alta']

class BorrarVideojuego(LoginRequiredMixin, DeleteView): 

    model = Videojuego
    success_url = '/videojuegos/'
    template_name = 'layouts/borrar_videojuego.html'

