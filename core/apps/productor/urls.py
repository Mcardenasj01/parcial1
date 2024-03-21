from django.urls import path

from apps.productor.views import ProductorCreate
from apps.productor.views import ProductorDelete
from apps.productor.views import ProductorList
from apps.productor.views import ProductorUpdate

app_name = "productor"

urlpatterns = [
    path('listar', ProductorList.as_view(), name='productor_listar'),
    path('crear', ProductorCreate.as_view(), name='productor_crear'),
    path('editar/<int:pk>', ProductorUpdate.as_view(), name='productor_editar'),
    path('eliminar/<int:pk>', ProductorDelete.as_view(), name='productor_eliminar'),
]