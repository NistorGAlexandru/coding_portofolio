"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
## URL - din proiect
from django.contrib import admin
from django.urls import path, include


from django.conf.urls.static import static
from django.conf import settings
from shop.sitemaps import ProductSitemaps, CategorySitemaps

from django.contrib.sitemaps.views import sitemap as sitemap_view

sitemap_context ={
    'sitemaps':{
        'products':ProductSitemaps,
        'categories':CategorySitemaps,
    }
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('cart/', include('cart.urls')),
    path('sitemap.xml', sitemap_view ,sitemap_context)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

