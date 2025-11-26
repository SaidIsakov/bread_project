from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  fields = ['name', 'slug']
  prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  fields = ('name', 'description', 'created_at', 'updated_up', 'price', 'image')
