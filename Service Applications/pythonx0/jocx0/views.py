from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def new_game_view(request):
    context = {
        'patratele' : range(1, 10)
    }
    return render(request, 'joc.html', context)

def insertx_view(request):
    pozitii = {
        "x":["5"],
        "0":["1"]
    }
    return JsonResponse(pozitii)