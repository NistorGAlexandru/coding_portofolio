
from django.contrib.sitemaps import  Sitemap

from .models import Product, Category

class ProductSitemaps(Sitemap):
    def items(self):
        return Product.objects.all()
    
class CategorySitemaps(Sitemap):
    def items(self):
        return Category.objects.all()