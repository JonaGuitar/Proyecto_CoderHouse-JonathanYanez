from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy

app_name = "Main"

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil', views.perfil, name='perfil'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='Main/password_change_done.html'), name='password_change_done'),    
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='Main/password_change.html', success_url=reverse_lazy('Main:password_change_done')), name='password_change'),
    
]