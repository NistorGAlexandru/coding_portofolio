from django.shortcuts import render
from django.http import HttpResponse

import random

# Create your views here.

def primul_view(request):
    return HttpResponse(f"Ati castigat {random.randint(1, 1000) * 1000} RON")

def javascript_view(request):
    return render(request, "index.html")