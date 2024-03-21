from django.db import models

from apps.productor.models import Productor

class Finca(models.Model):
    
    class Meta:
        verbose_name = 'Finca'
        verbose_name_plural = 'Fincas'
        
    numero_catrastro = models.CharField(max_length = 20, unique=True)
    municipio = models.CharField(max_length = 15)
    propietario = models.ForeignKey(Productor, null = True, blank = True, on_delete = models.CASCADE)
    
    REQUIRED_FIELDS = ['numero_catrastro', 'municipio']
    
    def __str__(self):
        return '{} {}'.format(self.numero_catrastro, self.municipio)
    