from django.contrib import admin
from django.urls import path, re_path
from Videogames import views 


urlpatterns = [

    path('', views.index, name = 'inicio'),
    path('videojuegos/about', views.about, name = 'acerca-de-nosotros'),
    path('videojuegos/catalogo', views.ver_catalogo, name = 'catalogo'),
    path('videojuegos/registrar', views.registrar_videojuego, name = 'registrar-videojuego'),
    path('videojuegos/editar/<int:pk>', views.EditarVideojuego.as_view(), name = 'editar_videojuego'),
    path('videojuegos/borrar/<int:pk>', views.BorrarVideojuego.as_view(), name = 'borrar_videojuego'),

]
