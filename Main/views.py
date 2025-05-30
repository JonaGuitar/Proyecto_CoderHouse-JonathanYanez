from django.shortcuts import render, redirect
from functools import wraps
from django.http import HttpResponseNotFound
from .forms import EditUserForm
from django.contrib.auth.decorators import login_required




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
def perfil (request):
    return render(request, "Main/perfil.html")



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
    
    