
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