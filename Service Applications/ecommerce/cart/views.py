from django.shortcuts import render, redirect
# Create your views here.

from .cart import Cart


def add_to_cart_view(request, product):
    #  logica de adaugat in cos
    print("request.POST=",request.POST)
    quantity = request.POST.get('quantity')
    print(quantity, product)
    cart =  Cart(request)
    cart.add_product(product, quantity)
    return redirect('cart_view_url')

def remove_product_view(request, product):
    cart =  Cart(request)
    cart.remove_product(product)
    return redirect('cart_view_url')

def clear_cart(request):
    print('clear cart a fost chemat')
    cart =  Cart(request)
    cart.clear_cart()
    return redirect('cart_view_url')


def cart_view(request):
    return render(request, 'cart.html')

