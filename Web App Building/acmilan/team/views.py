from django.shortcuts import render
import json
# Create your views here.

def dreamteam_view(request):
    with open("dreamteam.json", "r") as f:
        jucatori =  json.load(f)  

    context = {
        'jucatori':jucatori
    }
    return render(request= request, template_name="dreamteam.html", context = context)



def dreamteam_hardcodat_view(request):
    return render(request= request, template_name="dreamteam_hardcodat.html")

def lista_jucatori_view(request):
    with open("dreamteam.json", "r") as f:
        jucatori =  json.load(f)    

    context = {
        'nume_jucatori' : ['Dida', 'Oddo', 'Nesta'],
        'cea_mai_buna':False,
        
        'jucatori' :jucatori
        #   [[["Dida","12"]], [["Oddo","44"], ["Nesta","13"], ["Maldini","3"], ["Jankulovski","18"]],
                    #    [["Gattuso","8"], ["Pirlo","21"], ["Ambrosini","23"]],
                    #       [["Kaka","22"], ["Seedorf","10"]],
                    #        [["Inzaghi","9"]] ]
    }
    return render(request= request, template_name="lista_jucatori.html", context = context)




