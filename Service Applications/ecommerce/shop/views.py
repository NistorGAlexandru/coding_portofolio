from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Product, Category
# Create your views here.

from cart.cart import Cart
from cart.form import AddToCartForm

def product_details(request, slug):

    cart =  Cart(request)
    form = AddToCartForm()

    product = get_object_or_404(Product, slug=slug)

    context = {'product':product, 'form':form}
    return render(request, 'product_details.html', context)



def category_details_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products_in_category = Product.objects.filter(category=category)

    context = {
        'category':category,
        'products':products_in_category
    }
    return render(request, 'product_list.html' , context)


def sesiune_view(request):
    print(request.session)
    request.session['cart'] = 'hello world'
    # print(request.session['cart'])
    response =  HttpResponse("<h1>Raspuns...</h1>")
    return response

def cookie_view(request):
    print(request.COOKIES)
    print(request.COOKIES.get('sessionid'))
    response =  HttpResponse("<h1>Raspuns...</h1>")
    response.set_cookie("3", "1000")
    return response

def product_list_view(request):
    products = Product.objects.all()
    print("request.GET=", request.GET)
    print("request.session=", request.session.get("cart"))
    context = { 'products':products  }
    return render(request, 'product_list.html', context)

from rest_framework import generics
from .api.serializers import ProductSerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CreateNewProductView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()




