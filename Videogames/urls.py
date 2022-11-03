from django.contrib import admin
from django.urls import path, re_path
from Videogames import views 


urlpatterns = [
    # path('', views.index, name = 'inicio'),
    # path('catalogo', views.ver_catalogo, name = 'catalogo'),
    # path('videojuegos/registrar', views.registrar_videojuego, name = 'registrar-videojuego'),
    # path('videojuegos/editar/<int:id>', views.editar_videojuego, name = 'editar_videojuego'),
    # path('videojuegos/eliminar/<int:id>', views.borrar_videojuego, name = 'eliminar_videojuego')

    # URLS BASADAS EN VISTAS 

    path('', views.index, name = 'inicio'),
    path('videojuegos/', views.ListarVideojuegos.as_view(), name = 'catalogo'),
    path('videojuegos/registrar', views.RegistrarVideojuego.as_view(), name = 'registrar-videojuego'),
    path('videojuegos/editar/<int:pk>', views.EditarVideojuego.as_view(), name = 'editar_videojuego'),
    path('videojuegos/borrar/<int:pk>', views.BorrarVideojuego.as_view(), name = 'borrar_videojuego'),
    
   
    
    # path('videojuegos/eliminar/<int:id>', views., name = 'eliminar_videojuego')
    
]
 # se agregó un path con una expresión regular porque sino rompia porque le pasabas en el front juego en vez de object
#re_path(r'^videojuegos/editar/(?P<pk>[-\w]*)/$', views.EditarVideojuego.as_view(), name = 'editar_videojuego'),