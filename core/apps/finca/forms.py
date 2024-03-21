from django import forms
from apps.finca.models import Finca

class FincaForm(forms.ModelForm):

    class Meta:
        model = Finca
        
        fields = [
            'numero_catrastro' ,
            'municipio',
            'propietario',
        ]

        labels = {
                'numero_catrastro': 'Número de catrastro',
                'municipio': 'Municipio',
                'propietario': 'Propietario'
            }

        widgets = {
            'numero_catrastro': forms.TextInput(attrs={'class':'form-control'}),
            'municipio': forms.TextInput(attrs={'class':'form-control'}),
            'propietario': forms.Select(attrs={'class':'form-control'}),
        }