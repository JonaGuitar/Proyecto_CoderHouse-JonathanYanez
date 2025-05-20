from django.shortcuts import render, redirect
from .models import Post, Fabricante, TipoVehiculo
from .forms import PostForm, FabricanteForm, TipoVehiculoForm


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
            return redirect('Aplicacion:post_listar')
    else:
        form = PostForm()
    
    return render(request, 'Aplicacion/agregar_vehiculos.html', {'form': form})



def post_buscar(request):
    busqueda = request.GET.get("busqueda", None)
    
    if busqueda:
        post_buscar = Post.objects.filter(marca__icontains=busqueda)
    else:
        post_buscar = Post.objects.all()
        
    return render(request, "Aplicacion/buscar_vehiculos.html", context={"Posts": post_buscar})



# def post_agregar_fabricante(request):
#     if request.method == 'POST':
#         form = FabricanteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('Aplicacion:post_listar')
#     else:
#         form = FabricanteForm()
#     return render(request, 'Aplicacion/agregar_fabricante.html', {'form': form})


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






# def post_agregar_tipo(request):
#     if request.method == 'POST':
#         form = TipoVehiculoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('Aplicacion:post_listar')
#     else:
#         form = TipoVehiculoForm()
#     return render(request, 'Aplicacion/agregar_tipo.html', {'form': form})



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