from django import forms

from apps.vivero.models import Cultivo
from apps.vivero.models import LaborFertilizante
from apps.vivero.models import LaborHongo
from apps.vivero.models import LaborPlaga
from apps.vivero.models import Vivero

class CultivoForm(forms.ModelForm):

    class Meta:
        model = Cultivo
        
        fields = [
            'codigo_cultivo' ,
            'nombre_cultivo',
        ]

        labels = {
                'codigo_cultivo': 'Código del Cultivo',
                'nombre_cultivo': 'Nombre del Cultivo',
            }

        widgets = {
            'codigo_cultivo': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_cultivo': forms.TextInput(attrs={'class':'form-control'}),
        }
        
class ViveroForm(forms.ModelForm):

    class Meta:
        model = Vivero
        
        fields = [
            'codigo_vivero' ,
            'nombre_vivero',
            'cultivo',
            'propietario',
        ]

        labels = {
                'codigo_vivero': 'Código del Vivero',
                'nombre_vivero': 'Nombre del Vivero',
                'cultivo': 'Tipo de Cultivo',
                'propietario': 'Propietario'
            }

        widgets = {
            'codigo_vivero': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_vivero': forms.TextInput(attrs={'class':'form-control'}),
            'cultivo': forms.Select(attrs={'class':'form-control'}),
            'propietario': forms.Select(attrs={'class':'form-control'}),
        }
        
class LaborForm(forms.ModelForm):

    class Meta:
        model = LaborFertilizante
        fields = '__all__'

        labels = {
            'fecha_labor': 'Fecha de Labor',
            'cultivo': 'Cultivo',
            'descripcion_labor': 'Descripción de Labor'
        }

class LaborFertilizanteForm(LaborForm):

    class Meta:
        model = LaborFertilizante
        fields = '__all__'
        
        labels = {
            'codigo_producto_control': 'Código de Fertiliante',   
        }
        widgets = {
            'fecha_labor': forms.TextInput(attrs={'class':'form-control'}),
            'cultivo': forms.Select(attrs={'class':'form-control'}),
            'descripcion_labor': forms.Textarea(attrs={'class':'form-control', "row":"10"}),
            'codigo_producto_control': forms.Select(attrs={'class':'form-control'}),
        }
        
class LaborHongoForm(LaborForm):

    class Meta:
        model = LaborHongo
        fields = '__all__'
        
        labels = {
            'codigo_producto_control': 'Código de Hongo',   
        }
        widgets = {
            'fecha_labor': forms.TextInput(attrs={'class':'form-control'}),
            'cultivo': forms.Select(attrs={'class':'form-control'}),
            'descripcion_labor': forms.Textarea(attrs={'class':'form-control', "row":"10"}),
            'codigo_producto_control': forms.Select(attrs={'class':'form-control'}),
        }
        
class LaborPlagaForm(LaborForm):

    class Meta:
        model = LaborPlaga
        fields = '__all__'
        
        labels = {
            'codigo_producto_control': 'Código de Plaga',   
        }
        widgets = {
            'fecha_labor': forms.TextInput(attrs={'class':'form-control'}),
            'cultivo': forms.Select(attrs={'class':'form-control'}),
            'descripcion_labor': forms.Textarea(attrs={'class':'form-control', "row":"10"}),
            'codigo_producto_control': forms.Select(attrs={'class':'form-control'}),
        }