from django.shortcuts import render
from datetime import datetime
from .forms import AccessForm

# Create your views here.
def access_view(request):
    return render(request, 'access.html')

def rezultat_view(request):
    print(request.POST)
    print('varsta:', request.POST.get('birthday'))

    birthday = request.POST.get('birthday')
    varsta_in_zile = datetime.today() - datetime.fromisoformat(birthday)
    varsta = varsta_in_zile.days // 365.2425
    varsta = int(varsta)
    print(varsta)

    print('gen:', request.GET.get('gender'))
    gen = request.GET.get('gender')
    print('sex:', request.GET.get('sex'))
    sex = request.GET.get('sex')

    este_masculin = gen == "m" 

## Logica de business
    raspuns = varsta in range (16 + este_masculin * 2, 70)

    context = {
        'rezultat': raspuns
    }


    return render(request, 'rezultat.html', context)

def django_form_view(request):
    if request.method == "GET":
        form = AccessForm()
        context = {'form': form}

        return render(request, 'django_form.html', context)
    else:
        received_form = AccessForm(request.POST)
        if received_form.is_valid():
                context = {
                'raspuns': True
                }
                return render(request, 'rezultat.html', context)
        else:
            print('Validarea nu este corecta')