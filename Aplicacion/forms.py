from django import forms
from .models import Post, Fabricante, TipoVehiculo, DetalleVehiculo

  
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
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3 })
        }

      
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['marca', 'modelo', 'pais', 'fabricante', 'tipo_vehiculo']
        widgets = {
            'fabricante': forms.Select(attrs={'class': 'form-select'}),
            'tipo_vehiculo': forms.Select(attrs={'class': 'form-select'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'rows': 2}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
        }  
        
        
        
class DetalleVehiculoForm(forms.ModelForm):
    class Meta:
        model = DetalleVehiculo
        fields = [
            'version', 'motor', 'cilindrada', 'transmision', 'velocidades', 'combustible',
            'rendimiento_ciudad', 'rendimiento_carretera', 'rendimiento_mixto',
            'puertas', 'asientos', 'llantas', 'llantas_tamano'
        ]
        widgets = {
            'version': forms.TextInput(attrs={'class': 'form-control'}),
            'motor': forms.TextInput(attrs={'class': 'form-control'}),
            'cilindrada': forms.TextInput(attrs={'class': 'form-control'}),
            'transmision': forms.TextInput(attrs={'class': 'form-control'}),
            'velocidades': forms.NumberInput(attrs={'class': 'form-control'}),
            'combustible': forms.TextInput(attrs={'class': 'form-control'}),
            'rendimiento_ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'rendimiento_carretera': forms.TextInput(attrs={'class': 'form-control'}),
            'rendimiento_mixto': forms.TextInput(attrs={'class': 'form-control'}),
            'puertas': forms.NumberInput(attrs={'class': 'form-control'}),
            'asientos': forms.NumberInput(attrs={'class': 'form-control'}),
            'llantas': forms.TextInput(attrs={'class': 'form-control'}),
            'llantas_tamano': forms.NumberInput(attrs={'class': 'form-control'}),
        }
