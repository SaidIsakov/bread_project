from django.urls import path
from .views import IndexView, filter_products


urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('filter_products/', filter_products, name='filter_products'),
]
