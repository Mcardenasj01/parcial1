from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from apps.productor.models import Productor
from apps.productor.forms import ProductorForm

class ProductorList(ListView):
    model = Productor
    template_name = 'productor_list.html'
    paginate_by = 20
    
class ProductorCreate(CreateView):
    model = Productor
    form_class = ProductorForm
    template_name = 'productor/productor_form.html'
    success_url = reverse_lazy('productor:productor_listar')

class ProductorUpdate(UpdateView):
    model = Productor
    form_class = ProductorForm
    template_name = 'productor/productor_form.html'
    success_url = reverse_lazy('productor:productor_listar')

class ProductorDelete(DeleteView):
    model = Productor
    template_name = 'productor/productor_delete.html'
    success_url = reverse_lazy('productor:productor_listar')