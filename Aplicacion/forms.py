from django import forms
#from .models import Post
from .models import Post, Fabricante, TipoVehiculo

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['marca', 'modelo', 'pais']
        #fields = ['marca', 'modelo', 'pais', 'fabricante', 'tipo_vehiculo']
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            #'fabricante': forms.Select(attrs={'class': 'form-select'}),
            #'tipo_vehiculo': forms.Select(attrs={'class': 'form-select'}),
        }
        
        
class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ['nombre', 'pais_origen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'pais_origen': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        
class TipoVehiculoForm(forms.ModelForm):
    class Meta:
        model = TipoVehiculo
        fields = ['tipo', 'descripcion']
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }
