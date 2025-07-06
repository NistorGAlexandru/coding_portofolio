from django.shortcuts import render
from .models import Post
# Create your views here.

from cart.cart import Cart


def blog_list_view(request):

    blogs = Post.objects.all()
    context = {'blogs':blogs}

    

    
    return render(request, 'blog_list.html', context)

def blog_details_view(request, slug):

    post_detail = Post.objects.filter(slug=slug).first() 

    context = {"post":post_detail}

    return render(request, 'blog_details.html', context)
