from django.db import models

class ProductoControl(models.Model):
    
    class Meta:
        abstract = True
        
    codigo_producto_control = models.CharField(max_length = 15, unique=True)
    nombre_producto_control = models.CharField(max_length = 15, unique=True)
    registro_ica_producto_control = models.CharField(max_length = 15, unique=True)
    frecuencia_producto_control = models.IntegerField(default=0)
    valor_producto_control = models.IntegerField(default=0)
    
    def __str__(self):
        return '{} {}'.format(self.codigo_producto_control, self.nombre_producto_control )

class Fertilizante(ProductoControl):
    
    class Meta:
        verbose_name = 'Prodcuto Fertilizante'
        verbose_name_plural = 'Productos Fertilizantes'
        
    ultima_aplicacion_fertilizante = models.DateField()
    
class Hongo(ProductoControl):
    
    class Meta:
        verbose_name = 'Prodcuto Hongo'
        verbose_name_plural = 'Productos Hongos'
        
    nombre_hongo = models.CharField(max_length = 15)
    carencia_periodo_hongo = models.DateField()   
    
class Plaga(ProductoControl):
    
    class Meta:
        verbose_name = 'Prodcuto Plaga'
        verbose_name_plural = 'Productos Plagas'
        
    carencia_plaga = models.IntegerField(default=0)
               