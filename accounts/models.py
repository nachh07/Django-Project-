from django.db import models
from django.contrib.auth.models import User

class ExtensionUsuario(models.Model): 

    # nos permite relacionar los objetos en la propiedad User con una pk 
    # CASCADE = Si se borra el usuario que está relacionado la clase, borra el objeto
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    # para proyecto final descripción email etc
    #descripcion = models.TextField()