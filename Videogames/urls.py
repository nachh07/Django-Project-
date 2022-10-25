from django.contrib import admin
from django.urls import path
from Videogames import views 

urlpatterns = [
    path('', views.index, name = 'inicio'),
    path('catalogo', views.ver_catalogo, name = 'catalogo'),
    path('registrar-videojuego', views.registrar_videojuego, name = 'registrar-videojuego')
]