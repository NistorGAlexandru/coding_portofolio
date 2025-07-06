from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def about_us_view(request):
    return render(request, 'about_us.html')

def last_year_view(request):
    return render(request, 'last_year.html')

def contact_view(request):
    return render(request, 'contact.html')

