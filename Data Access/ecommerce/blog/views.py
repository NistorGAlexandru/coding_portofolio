from django.shortcuts import render
from .models import Post
from cart.cart import Cart
# Create your views here.


def blog_list_view(request):
     
    blogs = Post.objects.all()
    context = {'blogs':blogs}

    cart =  Cart(request)
    products =  cart.all_products()
    count = cart.count()
    context = {'products':products,
               'count': count}
    
    return render(request, 'blog_list.html', context)

def blog_details_view(request, slug):

    post_detail = Post.objects.filter(slug=slug).first() 

    context = {"post":post_detail}

    return render(request, 'blog_details.html', context)
