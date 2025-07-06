from .cart import Cart

def processing(request):
    cart =  Cart(request)
    products =  cart.all_products()
    count = cart.count()
    total = cart.total()
    context = {'products':products,
               'count': count,
               'total':total}
    return context