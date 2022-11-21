from django.contrib import admin
from django.urls import path, re_path
from Videogames import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index, name = 'inicio'),
    path('videojuegos/about', views.about, name = 'acerca-de-nosotros'),
    path('videojuegos/catalogo', views.ver_catalogo, name = 'catalogo'),
    path('videojuegos/registrar', views.registrar_videojuego, name = 'registrar-videojuego'),
    path('videojuegos/editar/<int:pk>', views.EditarVideojuego.as_view(), name = 'editar_videojuego'),
    path('videojuegos/borrar/<int:pk>', views.BorrarVideojuego.as_view(), name = 'borrar_videojuego'),
    path('videojuegos/detalles/<int:id>', views.ver_detalles, name = 'ver_detalles')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)