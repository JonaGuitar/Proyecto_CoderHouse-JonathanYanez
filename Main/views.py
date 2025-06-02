from django.shortcuts import render, redirect
from functools import wraps
from django.http import HttpResponseNotFound
from .forms import RegistroUsuarioForm, EditUserForm, UserChangeForm, MiFormularioPerfil, PerfilUsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PerfilUsuario


# Create your views here.
def index (request):
    return render(request, "Main/index.html")



def login_required_404(view_func):    
    @wraps(view_func)
    
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseNotFound(render(request, 'Main/404.html'))
        return view_func(request, *args, **kwargs)
    
    return wrapper





@login_required_404
def perfil(request):
    # Crea el perfil si no existe
    perfil, creado = PerfilUsuario.objects.get_or_create(user=request.user)
    
    form = MiFormularioPerfil(instance=request.user)
    return render(request, "Main/perfil.html", {
        'form': form,
        'perfil_usuario': perfil
    })
    


@login_required_404
def editar_perfil(request):
    perfil_usuario, _ = PerfilUsuario.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form_user = EditUserForm(request.POST, instance=request.user)
        form_perfil = PerfilUsuarioForm(request.POST, request.FILES, instance=perfil_usuario)

        if form_user.is_valid() and form_perfil.is_valid():
            form_user.save()
            form_perfil.save()
            return redirect("Main:perfil")
    else:
        form_user = EditUserForm(instance=request.user)
        form_perfil = PerfilUsuarioForm(instance=perfil_usuario)

    return render(request, 'Main/editar_perfil.html', {
        "form": form_user,
        "form_perfil": form_perfil
    })
    
    

 
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado con éxito.')
            return redirect("Main:registrar_usuario")  # Puedes redirigir a donde quieras
    else:
        form = RegistroUsuarioForm()
        
    return render(request, 'Main/registrar_usuario.html', {'form': form})
    