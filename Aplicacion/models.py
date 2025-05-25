from django.db import models
 
# Create your models here.
 
class Fabricante(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)

    def __str__(self):
        #return f"{self.nombre} - {self.pais_origen}"
        return f"{self.nombre}"
    
    
    
class TipoVehiculo(models.Model):
    tipo = models.CharField(max_length=100) 
    descripcion = models.TextField()

    def __str__(self):
        #return f"{self.tipo} - {self.descripcion}"
        return f"{self.tipo}"
    
   
    
class Post(models.Model):
    marca = models.CharField(max_length=100)   # ej: MG, Maxus, Roewe
    modelo = models.TextField()                 # ej: HS EV
    pais = models.TextField()
    fabricante = models.ForeignKey(Fabricante, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.SET_NULL, null=True, blank=True)    
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        fabricante_nombre = self.fabricante.nombre if self.fabricante else "Sin fabricante"
        tipo = self.tipo_vehiculo.tipo if self.tipo_vehiculo else "Sin tipo"
        return f"{self.marca} {self.modelo} - {fabricante_nombre} - {tipo} - {self.pais}"




    