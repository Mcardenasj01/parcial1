from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from apps.finca.models import Finca
from apps.finca.forms import FincaForm

class FincaList(ListView):
    model = Finca
    template_name = 'finca_list.html'
    paginate_by = 20
    
class FincaCreate(CreateView):
    model = Finca
    form_class = FincaForm
    template_name = 'finca/finca_form.html'
    success_url = reverse_lazy('finca:finca_listar')

class FincaUpdate(UpdateView):
    model = Finca
    form_class = FincaForm
    template_name = 'finca/finca_form.html'
    success_url = reverse_lazy('finca:finca_listar')

class FincaDelete(DeleteView):
    model = Finca
    template_name = 'finca/finca_delete.html'
    success_url = reverse_lazy('finca:finca_listar')