from django import forms

from apps.productoControl.models import ProductoControl
from apps.productoControl.models import Fertilizante
from apps.productoControl.models import Hongo
from apps.productoControl.models import Plaga

class ProductoControlForm(forms.ModelForm):

    class Meta:
        model = ProductoControl
        fields = '__all__'

        labels = {
            'codigo_producto_control': 'Código del Producto',
            'nombre_producto_control': 'Nombre de Producto',
            'registro_ica_producto_control': 'Registro ICA',
            'frecuencia_producto_control': 'Frecuencia aplicación del Producto en días',
            'valor_producto_control': 'Valor del Producto',
            }
        
class FertilizanteForm(ProductoControlForm):

    class Meta:
        model = Fertilizante
        fields = '__all__'
        
        labels = {
            'ultima_aplicacion_fertilizante': 'Última Fecha de Aplicación'
        }

        widgets = {
            'codigo_producto_control': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_producto_control': forms.TextInput(attrs={'class':'form-control'}),
            'registro_ica_producto_control': forms.TextInput(attrs={'class':'form-control'}),
            'frecuencia_producto_control': forms.NumberInput(attrs={'class':'form-control'}),
            'valor_producto_control': forms.NumberInput(attrs={'class':'form-control'}),
            'ultima_aplicacion_fertilizante': forms.TextInput(attrs={'class':'form-control'}),
        }

class HongoForm(ProductoControlForm):

    class Meta:
        model = Hongo
        fields = '__all__'

        labels = {
            'carencia_periodo_hongo': 'Carencia Hongo',
        }

        widgets = {
            'codigo_producto_control': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_producto_control': forms.TextInput(attrs={'class':'form-control'}),
            'registro_ica_producto_control': forms.TextInput(attrs={'class':'form-control'}),
            'frecuencia_producto_control': forms.NumberInput(attrs={'class':'form-control'}),
            'valor_producto_control': forms.NumberInput(attrs={'class':'form-control'}),
            'nombre_hongo': forms.TextInput(attrs={'class':'form-control'}),
            'carencia_periodo_hongo': forms.TextInput(attrs={'class':'form-control'}),
        }
               
class PlagaForm(ProductoControlForm):

    class Meta:
        model = Plaga
        fields = '__all__'

        labels = {
            'carencia_producto_control_plaga': 'Carencia'
        }

        widgets = {
            'codigo_producto_control': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_producto_control': forms.TextInput(attrs={'class':'form-control'}),
            'registro_ica_producto_control': forms.TextInput(attrs={'class':'form-control'}),
            'frecuencia_producto_control': forms.NumberInput(attrs={'class':'form-control'}),
            'valor_producto_control': forms.NumberInput(attrs={'class':'form-control'}),
            'carencia_plaga': forms.TextInput(attrs={'class':'form-control'}),
        }
        