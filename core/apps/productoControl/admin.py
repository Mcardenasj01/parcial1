from django.contrib import admin

from apps.productoControl.models import Plaga
"""
class ProductoControlPlagaAdmin(admin.ModelAdmin):
    list_display = ('codigo_producto_control', 'nombre_producto_control', 'registro_ica_producto_control', 'carencia_producto_control_plaga')
    search_fields = ('codigo_producto_control', 'registro_ica_producto_control')
    list_per_page = 25
"""
admin.site.register(Plaga)