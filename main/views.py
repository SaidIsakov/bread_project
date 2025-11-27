from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Product, Category
from django.http import JsonResponse
from .forms import ContactForm
from django.views import View


class IndexView(View):
    template_name = 'main/index.html'

    def get(self, request):
        context = {
            "products": Product.objects.all(),
            'categories': Category.objects.all(),
            'title': 'Любовь и Тесто',
            'form': ContactForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            "products": Product.objects.all(),
            'categories': Category.objects.all(),
            'title': 'Любовь и Тесто',
            'form': form
        }
        return render(request, self.template_name, context)



def filter_products(request):
    """AJAX функция для фильтрации товаров по категории"""
    category_id = request.GET.get('category')

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

