from django.test import TestCase

# Create your tests here.
import time

stiva = [0, 0, 0, 0]  # nivel = 0
stiva = [1, 2, 0, 0]  # nivel = 1
stiva = [1, 1, 0, 0]  #  nivel = 2
stiva = [1, 3, 2, 4]  # nivel = 4


def este_valida_mutarea(nivel, stiva):
    for i in range(nivel):
        if stiva[nivel] == stiva[i]:
            return False
        ## Diagonala principala (Stanga sus, dreapta jos)
        if abs(stiva[nivel] - stiva[i]) == abs(nivel - i):
            return False
        
        ## Diagonala secundara (Drapta sus, stanga jos)
        if abs(stiva[nivel] + nivel) == abs(stiva[i] + i):
            return False
    return True

        

def backtracking(N):
    stiva = [0] * N
    print(stiva)
    nivel = 0
    solutii = []
    while nivel >= 0:
        print("Nivel=", nivel, "stiva=", stiva)
        input()
        time.sleep(0.1)
        if nivel == N:
            solutii.append(stiva.copy())
            print('Solutie gasita')
            nivel -= 1
        elif stiva[nivel] < N:
            stiva[nivel] += 1
            if este_valida_mutarea(nivel, stiva):
                nivel += 1
                print('este valida mutarea')
        else:
            stiva[nivel] = 0
            nivel -= 1    
    return solutii


print(backtracking(N=4))