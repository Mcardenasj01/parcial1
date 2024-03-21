from django.urls import path

from apps.finca.views import FincaCreate
from apps.finca.views import FincaDelete
from apps.finca.views import FincaList
from apps.finca.views import FincaUpdate

app_name = "finca"

urlpatterns = [
    path('listar', FincaList.as_view(), name='finca_listar'),
    path('crear', FincaCreate.as_view(), name='finca_crear'),
    path('editar/<int:pk>', FincaUpdate.as_view(), name='finca_editar'),
    path('eliminar/<int:pk>', FincaDelete.as_view(), name='finca_eliminar'),
]