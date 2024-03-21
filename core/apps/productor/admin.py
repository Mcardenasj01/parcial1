from django.contrib import admin

from apps.productor.models import Productor

class ProductorAdmin(admin.ModelAdmin):
    list_display = ('documento', 'primer_nombre', 'segundo_nombre', 'telefono', 'email')
    search_fields = ('documento', 'telefono', 'email')
    list_per_page = 25

admin.site.register(Productor, ProductorAdmin)