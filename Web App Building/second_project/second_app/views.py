from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404

def view_exemplu(request):
    print('Functia view exemplu a fost chemata')
    return HttpResponse('Acesta este un exemplu')

def nume_intreg(request):
    return HttpResponse('Nistor Gabriel-Alexandru')

def view_404(request):
    raise Http404

def view_dublu(request, x):
    return HttpResponse(f'{x**2}')

def view_adunare(request, x, y):
    return HttpResponse(f'{x+y}')

def view_concatenare(request):
    print(request)
    print(request.GET)
    print(request.GET.get('cuvant1'))

    c1 = request.GET.get('cuvant1')
    c2 = request.GET.get('cuvant2')

    return HttpResponse(f"Ati comandat: {c1} cu {c2} ")