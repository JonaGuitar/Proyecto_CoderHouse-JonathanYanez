from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import PerfilUsuario


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Email")
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nombre de usuario")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Confirmar contraseña")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
        
class EditUserForm(UserChangeForm):
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, label='Apellido', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(required=True, label='Nombre Usuario', disabled=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(label='¿Activo?', required=False)
    is_staff = forms.BooleanField(label='¿Es staff?', required=False)
    is_superuser = forms.BooleanField(label='¿Es superusuario?', required=False)
    last_login = forms.DateTimeField(label='Último login', required=False, disabled=True, widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    date_joined = forms.DateTimeField(label='Fecha de registro', required=False, disabled=True, widget=forms.DateTimeInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'is_active', 'is_staff', 'is_superuser',
            'last_login', 'date_joined'
        ]        


    
class MiFormularioPerfil(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'is_active', 'is_staff', 'is_superuser',
                  'last_login', 'date_joined']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['disabled'] = True            
    
    
    


class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['avatar', 'biografia', 'link', 'fecha_nacimiento']
        widgets = {
            'biografia': forms.Textarea(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({'class': 'form-control'})
