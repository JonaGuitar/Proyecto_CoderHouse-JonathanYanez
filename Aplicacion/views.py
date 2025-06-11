from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Fabricante, TipoVehiculo, DetalleVehiculo
from .forms import PostForm, FabricanteForm, TipoVehiculoForm, DetalleVehiculoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from Main.views import login_required_404
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import CreateView, UpdateView
from django.http import Http404



def acerca(request):
    return render(request, 'Aplicacion/acercade.html')



def post_listar(request):
    post_listar = Post.objects.all()
    
    return render(request, "Aplicacion/listar_vehiculos.html", context={"Posts": post_listar})



def post_buscar(request):
    busqueda = request.GET.get("busqueda", None)
    se_realizo_busqueda = False
    post_buscar = Post.objects.none()

    if busqueda:
        se_realizo_busqueda = True
        post_buscar = Post.objects.filter(
            Q(marca__icontains=busqueda) |
            Q(modelo__icontains=busqueda) |
            Q(pais__icontains=busqueda)
        )

    return render(request, "Aplicacion/buscar_vehiculos.html", context={"Posts": post_buscar, "se_realizo_busqueda": se_realizo_busqueda})


 


@login_required_404
def post_agregar(request):
    fue_creado = False
    eliminado = request.GET.get('eliminado') == '1'  # 👈 Agrega esta línea

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Aplicacion/post_agregar?creado=1')  # redirige con un parámetro
    else:
        form = PostForm()

    if request.GET.get('creado') == '1':
        fue_creado = True

    vehiculos = Post.objects.all()
    fabricantes = Fabricante.objects.all()       
    tipos = TipoVehiculo.objects.all()           

    return render(request, 'Aplicacion/agregar_vehiculos.html', {
        'form': form,
        'vehiculos': vehiculos,
        'fabricantes': fabricantes,
        'tipos': tipos,
        'fue_creado': fue_creado,
        'eliminado': eliminado,  # 👈 Y pasa esto al template
    })

    



@login_required_404
def post_editar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Post, id=vehiculo_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('Aplicacion:post_agregar') 
    else:
        form = PostForm(instance=vehiculo)



@login_required_404
def post_eliminar_vehiculo(request, vehiculo_id):
    if request.method == 'POST':
        vehiculo = get_object_or_404(Post, id=vehiculo_id)
        vehiculo.delete()
        return redirect('/Aplicacion/post_agregar?eliminado=1') 

    return redirect('Aplicacion:post_agregar')
   
    
    


@login_required_404    
def post_agregar_fabricante(request):
    form = FabricanteForm()
    fue_creado = False
    eliminado = request.GET.get('eliminado') == '1'  # Flag para modal eliminación

    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            form.save()
            fue_creado = True
            form = FabricanteForm()

    fabricantes = Fabricante.objects.all().order_by('nombre')

    return render(request, 'Aplicacion/agregar_fabricante.html', {
        'form': form,
        'fabricantes': fabricantes,
        'fue_creado': fue_creado,
        'eliminado': eliminado,
    })

    
      
@login_required_404   
def post_editar_fabricante(request, fabricante_id):
    fabricante = get_object_or_404(Fabricante, id=fabricante_id)

    if request.method == 'POST':
        form = FabricanteForm(request.POST, instance=fabricante)
        if form.is_valid():
            form.save()
            return redirect('Aplicacion:post_agregar_fabricante')
    else:
        form = FabricanteForm(instance=fabricante)

  

@login_required_404
def post_eliminar_fabricante(request, fabricante_id):
    if request.method == 'POST':
        fabricante = get_object_or_404(Fabricante, id=fabricante_id)
        fabricante.delete()
        # Redirigir a la página con un parámetro GET para mostrar el modal de éxito
        url = reverse('Aplicacion:post_agregar_fabricante') + '?eliminado=1'
        return redirect(url)
    return redirect('Aplicacion:post_agregar_fabricante')
    





@login_required_404
def post_agregar_tipo(request):
    form = TipoVehiculoForm()
    fue_creado = False
    fue_eliminado = request.GET.get('eliminado') == '1'

    if request.method == 'POST':
        form = TipoVehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            fue_creado = True
            form = TipoVehiculoForm()

    tipos = TipoVehiculo.objects.all().order_by('tipo')
    return render(request, 'Aplicacion/agregar_tipo.html', {
        'form': form,
        'tipos': tipos,
        'fue_creado': fue_creado,
        'fue_eliminado': fue_eliminado,
    })
    
    
@login_required_404   
def post_editar_tipo(request, tipo_id):
    tipo = get_object_or_404(TipoVehiculo, id=tipo_id)

    if request.method == 'POST':
        form = TipoVehiculoForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('Aplicacion:post_agregar_tipo')
    else:
        form = TipoVehiculoForm(instance=tipo)    
    


@login_required_404   
def post_eliminar_tipo(request, tipo_id):
    if request.method == 'POST':
        tipo = get_object_or_404(TipoVehiculo, id=tipo_id)
        tipo.delete()
        return HttpResponseRedirect(reverse('Aplicacion:post_agregar_tipo') + '?eliminado=1')
    return redirect('Aplicacion:post_agregar_tipo')







class DetalleVehiculoCreateView(CreateView):
    model = DetalleVehiculo
    form_class = DetalleVehiculoForm
    template_name = 'Aplicacion/detalle_vehiculo_form.html'
    success_url = reverse_lazy('Aplicacion:post_agregar')

    def get_initial(self):
        initial = super().get_initial()
        vehiculo_id = self.request.GET.get('vehiculo_id')
        if vehiculo_id:
            initial['post'] = vehiculo_id
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

    def form_valid(self, form):
        post_id = self.request.POST.get('post')
        if post_id:
            try:
                post_instance = Post.objects.get(id=post_id)
                form.instance.post = post_instance
                messages.success(self.request, 'Detalle del vehículo guardado correctamente.')
                return super().form_valid(form)
            except Post.DoesNotExist:
                form.add_error(None, 'El vehículo seleccionado no existe.')
                return self.form_invalid(form)
        else:
            form.add_error(None, 'Debe seleccionar un vehículo.')
            return self.form_invalid(form)



class DetalleVehiculoUpdateView(UpdateView):
    model = DetalleVehiculo
    form_class = DetalleVehiculoForm
    template_name = 'Aplicacion/detalle_vehiculo_edit.html'
    success_url = reverse_lazy('Aplicacion:post_agregar')

    def get_object(self, queryset=None):
        vehiculo_id = self.request.GET.get('vehiculo_id')
        if not vehiculo_id:
            raise Http404("No se especificó vehículo")
        return get_object_or_404(DetalleVehiculo, post__id=vehiculo_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Detalle del vehículo actualizado correctamente.')
        return super().form_valid(form)










def login_modal(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            # Agregamos un mensaje para usar con SweetAlert2
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponse(status=405)

    
    
    
    
def logout_view(request):
    logout(request)
    
    return redirect('Main:index')  # Asegúrate que este nombre está en tu urls.py
    
    
