from django.contrib import admin

from apps.finca.models import Finca

class FincaAdmin(admin.ModelAdmin):
    
    list_display = ('numero_catrastro', 'municipio')
    search_fields = ('numero_catrastro', 'municipio')
    list_per_page = 25

admin.site.register(Finca, FincaAdmin)