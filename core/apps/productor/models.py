from django.db import models

class Productor(models.Model):
    
    class Meta:
        verbose_name = 'Productor'
        verbose_name_plural = 'Productores'
    
    documento = models.CharField(max_length = 10, unique=True)
    primer_nombre = models.CharField(max_length = 15)
    segundo_nombre = models.CharField(max_length = 15, blank=True, null=True)
    primer_apellido = models.CharField(max_length = 15)
    segundo_apellido = models.CharField(max_length = 15, blank=True, null=True)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    
    REQUIRED_FIELDS = ['documento', 'primer_nombre', 'primer_apellido']

    def __str__(self):
        return '{} {}'.format(self.primer_nombre, self.segundo_nombre)
