from django.urls import path

from apps.vivero.views import CultivoCreate
from apps.vivero.views import CultivoDelete
from apps.vivero.views import CultivoList
from apps.vivero.views import CultivoUpdate
from apps.vivero.views import LaborCreateFertilizante
from apps.vivero.views import LaborDetailFertilizante
from apps.vivero.views import LaborListFertilizante
from apps.vivero.views import LaborUpdateFertilizante
from apps.vivero.views import LaborCreateHongo
from apps.vivero.views import LaborDetailHongo
from apps.vivero.views import LaborListHongo
from apps.vivero.views import LaborUpdateHongo
from apps.vivero.views import LaborCreatePlaga
from apps.vivero.views import LaborDetailPlaga
from apps.vivero.views import LaborListPlaga
from apps.vivero.views import LaborUpdatePlaga
from apps.vivero.views import ViveroCreate
from apps.vivero.views import ViveroDelete
from apps.vivero.views import ViveroList
from apps.vivero.views import ViveroUpdate

app_name = "vivero"

urlpatterns = [
    path('cultivo/listar', CultivoList.as_view(), name='cultivo_listar'),
    path('cultivo/crear', CultivoCreate.as_view(), name='cultivo_crear'),
    path('cultivo/editar/<int:pk>', CultivoUpdate.as_view(), name='cultivo_editar'),
    path('cultivo/eliminar/<int:pk>', CultivoDelete.as_view(), name='cultivo_eliminar'),
    path('vivero/listar', ViveroList.as_view(), name='vivero_listar'),
    path('vivero/crear', ViveroCreate.as_view(), name='vivero_crear'),
    path('vivero/editar/<int:pk>', ViveroUpdate.as_view(), name='vivero_editar'),
    path('vivero/eliminar/<int:pk>', ViveroDelete.as_view(), name='vivero_eliminar'),
    path('laborFertilizante/listar', LaborListFertilizante.as_view(), name='laborFertilizante_listar'),
    path('laborFertilizante/crear', LaborCreateFertilizante.as_view(), name='laborFertilizante_crear'),
    path('laborFertilizante/editar/<int:pk>', LaborUpdateFertilizante.as_view(), name='laborFertilizante_editar'),
    path('laborFertilizante/detalle/<int:pk>', LaborDetailFertilizante.as_view(), name='laborFertilizante_detalle'),
    path('laborHongo/listar', LaborListHongo.as_view(), name='laborHongo_listar'),
    path('laborHongo/crear', LaborCreateHongo.as_view(), name='laborHongo_crear'),
    path('laborHongo/editar/<int:pk>', LaborUpdateHongo.as_view(), name='laborHongo_editar'),
    path('laborHongo/detalle/<int:pk>', LaborDetailHongo.as_view(), name='laborHongo_detalle'),
    path('laborPlaga/listar', LaborListPlaga.as_view(), name='laborPlaga_listar'),
    path('laborPlaga/crear', LaborCreatePlaga.as_view(), name='laborPlaga_crear'),
    path('laborPlaga/editar/<int:pk>', LaborUpdatePlaga.as_view(), name='laborPlaga_editar'),
    path('laborPlaga/detalle/<int:pk>', LaborDetailPlaga.as_view(), name='laborPlaga_detalle'),
]