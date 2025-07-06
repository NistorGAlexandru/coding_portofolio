from django.shortcuts import render
from django.http import HttpResponse
import re
import random

# Create your views here.

def random_color_view(request):
    r, g, b = [hex(random.randint(0, 255))[2:].zfill(2) for i in range(3)]
    return HttpResponse(f"<div style='background-color:#{r}{g}{b}'>   #{r}{g}{b}  </div>")

def random_color_view2(request):
    choices = [str(i) for i in range(10)] + list('ABCDEF')
    color = [random.choice(choices) for i in range(6)]
    print(color)
    color = "#"+"".join(color)
    return HttpResponse(f"<div style='background-color:{color}'> {color} </div>")


def color_view(request, color):
    return HttpResponse(f"<div style='background-color:{color}'> {color} </div>")

def rgb_color_view(request, red, green, blue):
    return HttpResponse(f"<div style='background-color:rgb({red},{green},{blue})'>   #{red}{green}{blue}  </div>")

def random_color_with_template_view(request):
    choices = [str(i) for i in range(10)] + list('ABCDEF')
    color = [random.choice(choices) for i in range(6)]
    print(color)
    color = "#"+"".join(color)
    return render(request, 'random_color.html', {'color':color})

def rgb_color_with_template(request, red, green, blue):
    return render(request, 'rgb_color.html', {'red':red}, {'green':green}, {'blue':blue})