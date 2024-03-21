from django.db import models

from apps.finca.models import Finca
from apps.productor.models import Productor
from apps.productoControl.models import Fertilizante
from apps.productoControl.models import Hongo
from apps.productoControl.models import Plaga

class Cultivo(models.Model):
    
    class Meta:
        verbose_name = 'Cultivo'
        verbose_name_plural = 'Cultivos'
        
    codigo_cultivo = models.CharField(max_length = 20, unique=True)
    nombre_cultivo = models.CharField(max_length = 20, unique=True)
    
    REQUIRED_FIELDS = ['codigo_cultivo', 'nombre_cultivo']
    
    def __str__(self):
        return '{} {}'.format(self.codigo_cultivo, self.nombre_cultivo)

class Vivero(models.Model):
    
    class Meta:
        verbose_name = 'Vivero'
        verbose_name_plural = 'Viveros'
        
    codigo_vivero = models.CharField(max_length = 20, unique=True)
    nombre_vivero = models.CharField(max_length = 20, unique=True)
    cultivo = models.ForeignKey(Cultivo, null = True, blank = True, on_delete = models.CASCADE)
    propietario = models.ForeignKey(Productor, null = True, blank = True, on_delete = models.CASCADE)
    
    REQUIRED_FIELDS = ['codigo_vivero', 'nombre_vivero']
    
    def __str__(self):
        return '{} {}'.format(self.codigo_vivero, self.nombre_vivero)

class Labor(models.Model):
    
    class Meta:
        abstract = True
        
    fecha_labor = models.DateTimeField()
    cultivo = models.ForeignKey(Cultivo, null = True, blank = True, on_delete = models.CASCADE)
    descripcion_labor = models.TextField(max_length=250)
    
class LaborFertilizante(Labor):
    
    class Meta:
        verbose_name = 'Labor Fertilizante'
        verbose_name_plural = 'Labor Fertilizantes'
        
    codigo_producto_control = models.ForeignKey(Fertilizante, null = True, blank = True, on_delete = models.CASCADE)

class LaborHongo(Labor):
    
    class Meta:
        verbose_name = 'Labor Hongo'
        verbose_name_plural = 'Labor Hongos'
    
    codigo_producto_control = models.ForeignKey(Hongo, null = True, blank = True, on_delete = models.CASCADE)

class LaborPlaga(Labor):
    
    class Meta:
        verbose_name = 'Labor Plaga'
        verbose_name_plural = 'Labor Plagas'
    
    codigo_producto_control = models.ForeignKey(Plaga, null = True, blank = True, on_delete = models.CASCADE)