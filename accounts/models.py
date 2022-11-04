from django.db import models
from django.contrib.auth.models import User

class ExtensionUsuario(models.Model):
    
    avatar = models.ImageField(upload_to='avatares',null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length = 50, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)