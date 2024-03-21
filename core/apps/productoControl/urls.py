from django.urls import path

from apps.productoControl.views import FertilizanteCreate
from apps.productoControl.views import FertilizanteDelete
from apps.productoControl.views import FertilizanteList
from apps.productoControl.views import FertilizanteUpdate
from apps.productoControl.views import HongoCreate
from apps.productoControl.views import HongoDelete
from apps.productoControl.views import HongoList
from apps.productoControl.views import HongoUpdate
from apps.productoControl.views import PlagaCreate
from apps.productoControl.views import PlagaDelete
from apps.productoControl.views import PlagaList
from apps.productoControl.views import PlagaUpdate

app_name = "productoControl"

urlpatterns = [
    path('fertilizante/listar', FertilizanteList.as_view(), name='fertilizante_listar'),
    path('fertilizante/crear', FertilizanteCreate.as_view(), name='fertilizante_crear'),
    path('fertilizante/editar/<int:pk>', FertilizanteUpdate.as_view(), name='fertilizante_editar'),
    path('fertilizante/eliminar/<int:pk>', FertilizanteDelete.as_view(), name='fertilizante_eliminar'),
    path('hongo/listar', HongoList.as_view(), name='hongo_listar'),
    path('hongo/crear', HongoCreate.as_view(), name='hongo_crear'),
    path('hongo/editar/<int:pk>', HongoUpdate.as_view(), name='hongo_editar'),
    path('hongo/eliminar/<int:pk>', HongoDelete.as_view(), name='hongo_eliminar'),
    path('plaga/listar', PlagaList.as_view(), name='plaga_listar'),
    path('plaga/crear', PlagaCreate.as_view(), name='plaga_crear'),
    path('plaga/editar/<int:pk>', PlagaUpdate.as_view(), name='plaga_editar'),
    path('plaga/eliminar/<int:pk>', PlagaDelete.as_view(), name='plaga_eliminar'),
]