from django.contrib import admin

# Register your models here.
from .models import Post, TipoVehiculo, Fabricante, DetalleVehiculo

admin.site.register(Post)
admin.site.register(TipoVehiculo)
admin.site.register(Fabricante)
admin.site.register(DetalleVehiculo)
