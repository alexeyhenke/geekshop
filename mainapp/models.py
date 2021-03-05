from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

class Product(models.Model):
    name = models.CharField(max_length=256)
    short_description = models.CharField(max_length=64, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images', blank=True)
    categories = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
