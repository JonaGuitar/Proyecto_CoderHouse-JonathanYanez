from django.shortcuts import render, redirect
from .models import Post, Fabricante, TipoVehiculo
from .forms import PostForm, FabricanteForm, TipoVehiculoForm
from django.shortcuts import redirect, get_object_or_404


def post_listar(request):
    post_listar = Post.objects.all()
    return render(request, "Aplicacion/listar_vehiculos.html", context={"Posts": post_listar})


def acerca(request):
    return render(request, 'Aplicacion/acercade.html')

 

def post_agregar(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Aplicacion:post_agregar')

    else:
        form = PostForm()

    vehiculos = Post.objects.all()
    fabricantes = Fabricante.objects.all()       # <-- Agregado
    tipos = TipoVehiculo.objects.all()           # <-- Agregado

    return render(request, 'Aplicacion/agregar_vehiculos.html', {
        'form': form,
        'vehiculos': vehiculos,
        'fabricantes': fabricantes,
        'tipos': tipos,
    })



def post_editar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Post, id=vehiculo_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('Aplicacion:post_agregar')  # Nombre correcto
    else:
        form = PostForm(instance=vehiculo)



def post_eliminar_vehiculo(request, vehiculo_id):
    if request.method == 'POST':
        vehiculo = get_object_or_404(Post, id=vehiculo_id)
        vehiculo.delete()
    return redirect('Aplicacion:post_agregar')  # Nombre correcto



def post_buscar(request):
    busqueda = request.GET.get("busqueda", None)
    
    if busqueda:
        post_buscar = Post.objects.filter(marca__icontains=busqueda)
    else:
        post_buscar = Post.objects.all()
        
    return render(request, "Aplicacion/buscar_vehiculos.html", context={"Posts": post_buscar})



def post_agregar_fabricante(request):
    form = FabricanteForm()

    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Aplicacion:post_agregar_fabricante')  # corregido

    fabricantes = Fabricante.objects.all().order_by('nombre')
    return render(request, 'Aplicacion/agregar_fabricante.html', {
        'form': form,
        'fabricantes': fabricantes
    })
    
      
    
def post_editar_fabricante(request, fabricante_id):
    fabricante = get_object_or_404(Fabricante, id=fabricante_id)

    if request.method == 'POST':
        form = FabricanteForm(request.POST, instance=fabricante)
        if form.is_valid():
            form.save()
            return redirect('Aplicacion:post_agregar_fabricante')
    else:
        form = FabricanteForm(instance=fabricante)

    

def post_eliminar_fabricante(request, fabricante_id):
    if request.method == 'POST':
        fabricante = get_object_or_404(Fabricante, id=fabricante_id)
        fabricante.delete()
    return redirect('Aplicacion:post_agregar_fabricante')  
    





def post_agregar_tipo(request):
    if request.method == 'POST':
        form = TipoVehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Aplicacion:post_agregar_tipo')  # redirige a sí misma
    else:
        form = TipoVehiculoForm()

    tipos = TipoVehiculo.objects.all().order_by('tipo')  # o el campo que uses

    return render(request, 'Aplicacion/agregar_tipo.html', {
        'form': form,
        'tipos': tipos,
    })

    

    
def post_editar_tipo(request, tipo_id):
    tipo = get_object_or_404(TipoVehiculo, id=tipo_id)

    if request.method == 'POST':
        form = TipoVehiculoForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('Aplicacion:post_agregar_tipo')
    else:
        form = TipoVehiculoForm(instance=tipo)    
    

    
def post_eliminar_tipo(request, tipo_id):
    if request.method == 'POST':
        tipo = get_object_or_404(TipoVehiculo, id=tipo_id)
        tipo.delete()
    return redirect('Aplicacion:post_agregar_tipo')      
    
    
