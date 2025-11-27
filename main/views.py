from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product, Category
from django.http import JsonResponse

class IndexView(TemplateView):
  template_name = 'main/index.html'


  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["products"] = Product.objects.all()
    context['categories'] = Category.objects.all()
    context['title'] = 'Любовь и Тесто'
    return context


def filter_products(request):
    """AJAX функция для фильтрации товаров по категории"""
    category_id = request.GET.get('category')

    # Если выбрана категория "all" или ничего не выбрано - показываем все товары
    if category_id == 'all' or not category_id:
        products = Product.objects.all()
    else:
        # Фильтруем товары по выбранной категории
        products = Product.objects.filter(category_id=category_id)

    # Преобразуем товары в данные для JSON
    products_data = []
    for product in products:
        products_data.append({
            'id': product.id,
            'name': product.name,
            'description': product.description or '',
            'price': str(product.price) if product.price else '',
            'image_url': product.image.url if product.image else 'Нет изображения',
        })

    return JsonResponse({
        'products': products_data
    })
