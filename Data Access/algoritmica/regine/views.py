from django.shortcuts import render, redirect
from django.http import JsonResponse
# Create your views here.

from .backtracking import backtracking

def json_spa_chess_table_view(request, N = 8):
    solutii = backtracking(N)
    prima_solutie = solutii[0]
    prima_solutie_shiftata = [ i + k * N - 1 for k, i in enumerate(prima_solutie) ]

    context = {
        'N_p': N**2,
        'range_N_p': range( N**2),
        'N' : N,
        'range_N': range(N),
        'solutii': solutii,
        'len_solutii':len(solutii),
        'prima_solutie': prima_solutie,
        'prima_solutie_shiftata': prima_solutie_shiftata

    }
    return render(request, 'json_spa_chess_table.html')

def spa_chess_table_view(request, N = 8):
    solutii = backtracking(N)
    prima_solutie = solutii[0]
    prima_solutie_shiftata = [ i + k * N - 1 for k, i in enumerate(prima_solutie) ]

    context = {
        'N_p': N**2,
        'range_N_p': range( N**2),
        'N' : N,
        'range_N': range(N),
        'solutii': solutii,
        'len_solutii':len(solutii),
        'prima_solutie': prima_solutie,
        'prima_solutie_shiftata': prima_solutie_shiftata

    }

    return render(request, 'chess_table.html', context)

def chess_table_view(request, N = 8, sol_no = 0):
    solutii = backtracking(N)
    if sol_no < 0:
        return redirect("chess_table_url_with_sol_no", N, len(solutii) - 1)
    if sol_no > len(solutii) - 1:
        return redirect("chess_table_url_with_sol_no", N, 0)
    else:
        prima_solutie = solutii[sol_no]
    prima_solutie_shiftata = [ i + k * N - 1 for k, i in enumerate(prima_solutie) ]

    context = {
        'N_p': N**2,
        'range_N_p': range( N**2),
        'N' : N,
        'sol_no':sol_no,
        'range_N': range(N),
        'solutii': solutii,
        'len_solutii':len(solutii),
        'prima_solutie': prima_solutie,
        'prima_solutie_shiftata': prima_solutie_shiftata

    }

    return render(request, 'spa_chess_table.html', context)


def json_chess_table_view(request, N = 8):
    response = {"solutii": backtracking(N), 
     "N":N}
    return JsonResponse(response)

