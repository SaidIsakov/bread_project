from django.contrib import admin
from .models import Category, Product, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  fields = ['name', 'slug']
  prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  fields = ('name', 'description', 'price', 'image', 'category')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = ['name', 'email', 'phon_number', 'message']
