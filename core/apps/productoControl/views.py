from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from apps.productoControl.forms import FertilizanteForm
from apps.productoControl.forms import HongoForm
from apps.productoControl.forms import PlagaForm
from apps.productoControl.models import Fertilizante
from apps.productoControl.models import Hongo
from apps.productoControl.models import Plaga

class FertilizanteCreate(CreateView):
    model = Fertilizante
    form_class = FertilizanteForm
    template_name = 'fertilizante/fertilizante_form.html'
    success_url = reverse_lazy('fertilizante:fertilizante_listar')

class FertilizanteDelete(DeleteView):
    model = Fertilizante
    template_name = 'fertilizante/fertilizante_delete.html'
    success_url = reverse_lazy('fertilizante:fertilizante_listar')

class FertilizanteList(ListView):
    model = Fertilizante
    template_name = 'fertilizante/fertilizante_list.html'
    paginate_by = 20
        
class FertilizanteUpdate(UpdateView):
    model = Fertilizante
    form_class = FertilizanteForm
    template_name = 'fertilizante/fertilizante_form.html'
    success_url = reverse_lazy('fertilizante:fertilizante_listar')
    
class HongoCreate(CreateView):
    model = Hongo
    form_class = HongoForm
    template_name = 'hongo/hongo_form.html'
    success_url = reverse_lazy('hongo:hongo_listar')

class HongoDelete(DeleteView):
    model = Hongo
    template_name = 'hongo/hongo_delete.html'
    success_url = reverse_lazy('hongo:hongo_listar')
    
class HongoList(ListView):
    model = Hongo
    template_name = 'hongo/hongo_list.html'
    paginate_by = 20
    
class HongoUpdate(UpdateView):
    model = Hongo
    form_class = HongoForm
    template_name = 'hongo/hongo_form.html'
    success_url = reverse_lazy('hongo:hongo_listar')
        
class PlagaCreate(CreateView):
    model = Plaga
    form_class = PlagaForm
    template_name = 'plaga/plaga_form.html'
    success_url = reverse_lazy('plaga:plaga_listar')
    
class PlagaDelete(DeleteView):
    model = Plaga
    template_name = 'plaga/plaga_delete.html'
    success_url = reverse_lazy('plaga:plaga_listar')

class PlagaList(ListView):
    model = Plaga
    template_name = 'plaga/plaga_list.html'
    paginate_by = 20
       
class PlagaUpdate(UpdateView):
    model = Plaga
    form_class = PlagaForm
    template_name = 'plaga/plaga_form.html'
    success_url = reverse_lazy('plaga:plaga_listar')

