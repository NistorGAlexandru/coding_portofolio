from django.shortcuts import render
from .forms import CNPForm
# Create your views here.

from django.http import HttpResponse

def validare_cnp_view(request):
    context = {}
    if request.method == "POST":
        print(request.POST)
        received_form = CNPForm(request.POST)
        if received_form.is_valid():
            context['rezultat'] = "Are access"
        else:
            context['rezultat'] = "CNP-ul NU are access"
    
    form = CNPForm()
    context['form'] =  form
    return render(request, 'validare.html', context)