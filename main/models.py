from django.db import models
from django.utils.text import slugify

class Category(models.Model):
  name = models.CharField(max_length=20)
  slug = models.SlugField(max_length=80, unique=True)

  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

  def __str__(self):
      return self.name

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    super().save(*args, **kwargs)


class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=300, blank=True, null=True)
  image = models.ImageField(upload_to='product_image', blank=True, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'Product'
    verbose_name_plural = 'Products'

  def __str__(self):
      return self.name


class Contact(models.Model):
  STATUS_CHOICES = [
        ('new', 'Новое'),
        ('processed', 'Обработано'),
        ('rejected', 'Отклонено'),
    ]
  name = models.CharField(max_length=20)
  phon_number = models.CharField(max_length=20)
  email = models.EmailField()
  message = models.TextField(max_length=100, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='new'
  )
