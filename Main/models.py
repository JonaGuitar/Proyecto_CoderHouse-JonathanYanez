from django.db import models
from django.contrib.auth.models import User



class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    biografia = models.TextField(max_length=500, blank=True)
    link = models.URLField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'
