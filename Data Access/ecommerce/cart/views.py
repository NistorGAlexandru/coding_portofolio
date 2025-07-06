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



def cart_view(request):
    cart =  Cart(request)
    products =  cart.all_products()
    total = cart.total()
    context = {'products':products,
               'total': total}
    print("Avem ", len(products),"produse", products)
    return render(request, 'cart.html', context)