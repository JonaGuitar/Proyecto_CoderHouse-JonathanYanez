from django.shortcuts import render, redirect
from functools import wraps
from django.http import HttpResponseNotFound
from .forms import RegistroUsuarioForm, EditUserForm, UserChangeForm, MiFormularioPerfil
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
    form = MiFormularioPerfil(instance=request.user)
    return render(request, "Main/perfil.html", {'form': form})



@login_required_404
def editar_perfil(request):
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("Main:perfil")
    else:
        form = EditUserForm(instance=request.user)

    return render(request, 'Main/editar_perfil.html', {"form": form})
    
    

 
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
    