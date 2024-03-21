from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from apps.vivero.models import Cultivo
from apps.vivero.models import LaborFertilizante
from apps.vivero.models import LaborHongo
from apps.vivero.models import LaborPlaga
from apps.vivero.models import Vivero
from apps.vivero.forms import CultivoForm
from apps.vivero.forms import LaborFertilizanteForm
from apps.vivero.forms import LaborHongoForm
from apps.vivero.forms import LaborPlagaForm
from apps.vivero.forms import ViveroForm

class CultivoList(ListView):
    model = Cultivo
    template_name = 'cultivo/cultivo_list.html'
    paginate_by = 20

class CultivoCreate(CreateView):
    model = Cultivo
    form_class = CultivoForm
    template_name = 'cultivo/cultivo_form.html'
    success_url = reverse_lazy('cultivo:cultivo_listar')

class CultivoUpdate(UpdateView):
    model = Cultivo
    form_class = CultivoForm
    template_name = 'cultivo/cultivo_form.html'
    success_url = reverse_lazy('cultivo:cultivo_listar')
    
class CultivoDelete(DeleteView):
    model = Cultivo
    template_name = 'cultivo/cultivo_delete.html'
    success_url = reverse_lazy('cultivo:cultivo_listar')    

class ViveroList(ListView):
    model = Vivero
    template_name = 'vivero/vivero_list.html'
    paginate_by = 20
    
class ViveroCreate(CreateView):
    model = Vivero
    form_class = ViveroForm
    template_name = 'vivero/vivero_form.html'
    success_url = reverse_lazy('vivero:vivero_listar')
    
class ViveroUpdate(UpdateView):
    model = Vivero
    form_class = ViveroForm
    template_name = 'vivero/vivero_form.html'
    success_url = reverse_lazy('vivero:vivero_listar')
    
class ViveroDelete(DeleteView):
    model = Vivero
    template_name = 'vivero/vivero_delete.html'
    success_url = reverse_lazy('vivero:vivero_listar') 
    
class LaborCreateFertilizante(CreateView):
    model = LaborFertilizante
    form_class = LaborFertilizanteForm
    template_name = 'laborFertilizante/laborFertilizante_form.html'
    success_url = reverse_lazy('laborFertilizante:laborFertilizante_listar')
    
class LaborDetailFertilizante(DetailView):
    model = LaborFertilizante
    template_name = 'laborFertilizante/laborFertilizante_detail.html'
    success_url = reverse_lazy('laborFertilizante:laborFertilizante_listar') 
    
class LaborListFertilizante(ListView):
    model = LaborFertilizante
    template_name = 'laborFertilizante/laborFertilizante_list.html'
    paginate_by = 20
    
class LaborUpdateFertilizante(UpdateView):
    model = LaborFertilizante
    form_class = LaborFertilizanteForm
    template_name = 'laborFertilizante/laborFertilizante_form.html'
    success_url = reverse_lazy('laborFertilizante:laborFertilizante_listar')

class LaborCreateHongo(CreateView):
    model = LaborHongo
    form_class = LaborHongoForm
    template_name = 'laborHongo/laborHongo_form.html'
    success_url = reverse_lazy('laborHongo:laborHongo_listar')
    
class LaborDetailHongo(DetailView):
    model = LaborHongo
    template_name = 'laborHongo/laborHongo_detail.html'
    success_url = reverse_lazy('laborHongo:laborHongo_listar') 
        
class LaborListHongo(ListView):
    model = LaborHongo
    template_name = 'laborHongo/laborHongo_list.html'
    paginate_by = 20
    
class LaborUpdateHongo(UpdateView):
    model = LaborHongo
    form_class = LaborHongoForm
    template_name = 'laborHongo/laborHongo_form.html'
    success_url = reverse_lazy('laborHongo:laborHongo_listar')
    
class LaborCreatePlaga(CreateView):
    model = LaborPlaga
    form_class = LaborPlagaForm
    template_name = 'laborPlaga/laborPlaga_form.html'
    success_url = reverse_lazy('laborPlaga:laborPlaga_listar')
    
class LaborDetailPlaga(DetailView):
    model = LaborPlaga
    template_name = 'laborPlaga/laborPlaga_detail.html'
    success_url = reverse_lazy('laborPlaga:laborPlaga_listar') 
    
class LaborListPlaga(ListView):
    model = LaborPlaga
    template_name = 'laborPlaga/laborPlaga_list.html'
    paginate_by = 20
    
class LaborUpdatePlaga(UpdateView):
    model = LaborPlaga
    form_class = LaborPlagaForm
    template_name = 'laborPlaga/laborPlaga_form.html'
    success_url = reverse_lazy('laborPlaga:laborPlaga_listar')