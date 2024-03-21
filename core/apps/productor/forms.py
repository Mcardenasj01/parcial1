from django import forms

from apps.productor.models import Productor

class ProductorForm(forms.ModelForm):

    class Meta:
        model = Productor
        
        fields = [
            'documento' ,
            'primer_nombre',
            'segundo_nombre',
            'primer_apellido',
            'segundo_apellido',
            'telefono',
            'email',
        ]

        labels = {
                'documento': 'Documento',
                'primer_nombre': 'Primer Nombre',
                'segundo_nombre': 'Segundo Nombre',
                'primer_apellido': 'Primer Apellido',
                'segundo_apellido': 'Segundo Apellido',
                'telefono': 'Teléfono',
                'email': 'Email',
            }

        widgets = {
            'documento': forms.TextInput(attrs={'class':'form-control'}),
            'primer_nombre': forms.TextInput(attrs={'class':'form-control'}),
            'segundo_nombre': forms.TextInput(attrs={'class':'form-control'}),
            'primer_apellido': forms.TextInput(attrs={'class':'form-control'}),
            'segundo_apellido': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }