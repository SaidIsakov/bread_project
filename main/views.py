from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product, Category


class IndexView(TemplateView):
  template_name = 'main/index.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["products"] = Product.objects.all()
      context['categories'] = Category.objects.all()
      return context
