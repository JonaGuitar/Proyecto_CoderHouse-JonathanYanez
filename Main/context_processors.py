from .models import PerfilUsuario

def avatar_usuario(request):
    if request.user.is_authenticated:
        perfil = PerfilUsuario.objects.filter(user=request.user).first()
        return {'avatar_usuario': perfil.avatar.url if perfil and perfil.avatar else None}
    return {}
