from django.db import models
 
# Create your models here.
 
class Fabricante(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.pais_origen}"
    
    
    
class TipoVehiculo(models.Model):
    tipo = models.CharField(max_length=100)  # Ej: SUV, Sedán, Pickup
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.tipo} {self.descripcion}"
    

class Post(models.Model): 
    marca = models.CharField(max_length=100)
    modelo = models.TextField()
    pais = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.marca} {self.modelo} {self.pais}"



    