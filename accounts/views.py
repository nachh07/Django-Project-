from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
# from django.contrib.auth import login as django_login
from accounts.forms import MiFormularioDeCreacion, EditarPerfilFormulario, MiCambioDePassword
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from accounts.models import ExtensionUsuario

def user_login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario) 
            extensionusuario, es_nuevo = ExtensionUsuario.objects.get_or_create(user=request.user)
            return redirect('inicio')
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'formulario': formulario})

def registrar(request):
    
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = MiFormularioDeCreacion()
    
    return render(request, 'accounts/registrar.html', {'formulario': formulario})

@login_required
def perfil(request):
    return render(request, 'accounts/perfil.html')

@login_required
def editar_perfil(request):
    
    user = request.user
    
    if request.method == 'POST':
        formulario = EditarPerfilFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            data_nueva = formulario.cleaned_data
            user.username = data_nueva['username']
            user.first_name = data_nueva['first_name']
            user.last_name = data_nueva['last_name']
            user.email = data_nueva['email']
            if data_nueva['avatar'] is not None: 
                user.extensionusuario.avatar = data_nueva['avatar']
            if len(data_nueva['descripcion']) > 0: 
                user.extensionusuario.descripcion = data_nueva['descripcion']
            else:
                user.extensionusuario.descripcion = 'Sin descripción'
            
            user.extensionusuario.save()
            user.save()
            return redirect('perfil')
        
    else:
        formulario = EditarPerfilFormulario(
            initial={
                'username' : user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'avatar': user.extensionusuario.avatar,
                'descripcion': user.extensionusuario.descripcion
            }
        )
    return render(request, 'accounts/editar_perfil.html', {'formulario': formulario})


class CambiarPassowrd(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/cambiar_contraseña.html'
    success_url = '/accounts/perfil/'
    form_class = MiCambioDePassword
