from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .models import LivroVisitas, Produto, Projetos
from .forms import LivroVisitasModelForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['projetos'] = Projetos.objects.order_by('?').all()
        return context


class ProdutosView(TemplateView):
    template_name = 'produtos.html'

    def get_context_data(self, **kwargs):
        context = super(ProdutosView, self).get_context_data(**kwargs)
        context['produtos'] = Produto.objects.order_by('?').all()
        return context


class TesteView(TemplateView):
    template_name = 'teste.html'
# Create your views here.


class VisitasView(TemplateView):
    template_name = 'visitas.html'

    def get_context_data(self, **kwargs):
        context = super(VisitasView, self).get_context_data(**kwargs)
        context['visitas'] = LivroVisitas.objects.all()
        return context


class VisitasFormView(FormView):
    template_name = 'visitasform.html'
    form_class = LivroVisitasModelForm
    success_url = reverse_lazy('visitas')

    def get_context_data(self, **kwargs):
        form = LivroVisitasModelForm
        context = {
            'form': form
        }
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




