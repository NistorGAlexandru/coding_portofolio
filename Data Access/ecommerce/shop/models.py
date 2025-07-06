from django.db import models

# Create your models here.

class Category(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):

    def __str__(self):
        return self.name
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)
    available = models.BooleanField(default=True)
    
    image = models.ImageField(upload_to='products', null=True)
    