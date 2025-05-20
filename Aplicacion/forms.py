from django import forms
#from .models import Post
from .models import Post, Fabricante, TipoVehiculo

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['marca', 'modelo', 'pais']
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
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
        
        
# from django import forms
# from .models import Post, TipoVehiculo, Fabricante

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['marca', 'modelo', 'pais', 'tipo', 'fabricante']
#         widgets = {
#             'marca': forms.TextInput(attrs={'class': 'form-control'}),
#             'modelo': forms.TextInput(attrs={'class': 'form-control'}),
#             'pais': forms.TextInput(attrs={'class': 'form-control'}),
#             'tipo': forms.Select(attrs={'class': 'form-control'}),
#             'fabricante': forms.Select(attrs={'class': 'form-control'}),
#         }
        
        
# from django import forms
# from .models import Post, Fabricante, TipoVehiculo

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = '__all__'

# class FabricanteForm(forms.ModelForm):
#     class Meta:
#         model = Fabricante
#         fields = '__all__'

# class TipoVehiculoForm(forms.ModelForm):
#     class Meta:
#         model = TipoVehiculo
#         fields = '__all__'