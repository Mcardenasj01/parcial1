from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView

from siav import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productor/', include('apps.productor.urls')),
    path('fertilizante/', include('apps.productoControl.urls', namespace='fertilizante')),
    path('hongo/', include('apps.productoControl.urls', namespace='hongo')),
    path('plaga/', include('apps.productoControl.urls', namespace='plaga')),
    path('finca/', include('apps.finca.urls')),
    path('cultivo/', include('apps.vivero.urls', namespace='cultivo')),
    path('vivero/', include('apps.vivero.urls', namespace='vivero')),
    path('laborFertilizante/', include('apps.vivero.urls', namespace='laborFertilizante')),
    path('laborHongo/', include('apps.vivero.urls', namespace='laborHongo')),
    path('laborPlaga/', include('apps.vivero.urls', namespace='laborPlaga')),
    path('admin/', admin.site.urls),
]
   