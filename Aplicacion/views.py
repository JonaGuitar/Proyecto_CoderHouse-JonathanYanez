from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Fabricante, TipoVehiculo
from .forms import PostForm, FabricanteForm, TipoVehiculoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def acerca(request):
    return render(request, 'Aplicacion/acercade.html')


def post_listar(request):
    post_listar = Post.objects.all()
    return render(request, "Aplicacion/listar_vehiculos.html", context={"Posts": post_listar})


def post_buscar(request):
    busqueda = request.GET.get("busqueda", None)
    
    if busqueda:
        post_buscar = Post.objects.filter(marca__icontains=busqueda)
    else:
        post_buscar = Post.objects.all()
        
    return render(request, "Aplicacion/buscar_vehiculos.html", context={"Posts": post_buscar})


 
#@login_required
def post_agregar(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Aplicacion:post_agregar')

    else:
        form = PostForm()

    vehiculos = Post.objects.all()
    fabricantes = Fabricante.objects.all()       
    tipos = TipoVehiculo.objects.all()           

    return render(request, 'Aplicacion/agregar_vehiculos.html', {
        'form': form,
        'vehiculos': vehiculos,
        'fabricantes': fabricantes,
        'tipos': tipos,
    })


#@login_required
def post_editar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Post, id=vehiculo_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('Aplicacion:post_agregar') 
    else:
        form = PostForm(instance=vehiculo)


#@login_required
def post_eliminar_vehiculo(request, vehiculo_id):
    if request.method == 'POST':
        vehiculo = get_object_or_404(Post, id=vehiculo_id)
        vehiculo.delete()
    return redirect('Aplicacion:post_agregar')




#@login_required
def post_agregar_fabricante(request):
    form = FabricanteForm()

    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Aplicacion:post_agregar_fabricante') 

    fabricantes = Fabricante.objects.all().order_by('nombre')
    return render(request, 'Aplicacion/agregar_fabricante.html', {
        'form': form,
        'fabricantes': fabricantes
    })
    
    
      
#@login_required    
def post_editar_fabricante(request, fabricante_id):
    fabricante = get_object_or_404(Fabricante, id=fabricante_id)

    if request.method == 'POST':
        form = FabricanteForm(request.POST, instance=fabricante)
        if form.is_valid():
            form.save()
            return redirect('Aplicacion:post_agregar_fabricante')
    else:
        form = FabricanteForm(instance=fabricante)

    
    
#@login_required
def post_eliminar_fabricante(request, fabricante_id):
    if request.method == 'POST':
        fabricante = get_object_or_404(Fabricante, id=fabricante_id)
        fabricante.delete()
    return redirect('Aplicacion:post_agregar_fabricante')  
    




#@login_required
def post_agregar_tipo(request):
    if request.method == 'POST':
        form = TipoVehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Aplicacion:post_agregar_tipo')  
    else:
        form = TipoVehiculoForm()

    tipos = TipoVehiculo.objects.all().order_by('tipo')  

    return render(request, 'Aplicacion/agregar_tipo.html', {
        'form': form,
        'tipos': tipos,
    })

    

#@login_required    
def post_editar_tipo(request, tipo_id):
    tipo = get_object_or_404(TipoVehiculo, id=tipo_id)

    if request.method == 'POST':
        form = TipoVehiculoForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('Aplicacion:post_agregar_tipo')
    else:
        form = TipoVehiculoForm(instance=tipo)    
    


#@login_required    
def post_eliminar_tipo(request, tipo_id):
    if request.method == 'POST':
        tipo = get_object_or_404(TipoVehiculo, id=tipo_id)
        tipo.delete()
    return redirect('Aplicacion:post_agregar_tipo')





def login_modal(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(request.META.get('HTTP_REFERER', '/'))  # Redirige a la página anterior
        else:
            return render(request, 'login_error.html', {'error': 'Credenciales inválidas'})
    else:
        return HttpResponse(status=405)  # Método no permitido si no es POST
    
    
