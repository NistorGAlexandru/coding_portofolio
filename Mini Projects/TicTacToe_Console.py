
demo = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

tabla =  [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
# tabla = [[" "] * 3]  * 3
print(tabla)

def printeaza_tabla(tabla):
    joc = f"""
     {tabla[0][0]} | {tabla[0][1]} | {tabla[0][2]}
    ---|---|---
     {tabla[1][0]} | {tabla[1][1]} | {tabla[1][2]}
    ---|---|--- 
     {tabla[2][0]} | {tabla[2][1]} | {tabla[2][2]}
    """
    return joc

print("X - incepe")
incepe_X = True
este_randul_lui_X = True

while True:

    alegere = input(f"Alegeti pozitia {printeaza_tabla(demo)}")
    print(alegere)

    while alegere not in [str(i) for i in range(1, 10)]:
        alegere = input(f"Alegeti pozitia {printeaza_tabla(demo)}")

    alegere = int(alegere)

    index_0 = (alegere-1) // 3 
    index_1 = (alegere-1) % 3

    if tabla[index_0][index_1] not in ['X', '0']:
        tabla[index_0][index_1] = 'X' if este_randul_lui_X else '0'
        print(printeaza_tabla(tabla))
        este_randul_lui_X = not este_randul_lui_X
    else:
        print("Nu se poate asa ceva")


    ### Remiza?? 
    este_terminat = True
    for linie in tabla:
        for pozitie in linie:
            if pozitie == " ":
                este_terminat = False 

    a_castigat_x, a_castigat_y = False,  False

    ### Orizontala
    for i0 in range(3):
        if tabla[i0][0] == tabla[i0][1] == tabla[i0][2] == "X":
            print("A castigat x")
            a_castigat_x = True
        elif tabla[i0][0] == tabla[i0][1] == tabla[i0][2] == "0":
            print("A castigat 0")
            a_castigat_y = True

    ### Verticala
    for i1 in range(3):
        if tabla[0][i1] == tabla[1][i1] == tabla[2][i1] == "X":
            print("A castigat x")
            a_castigat_x = True
        elif tabla[0][i1] == tabla[1][i1] == tabla[2][i1] == "0":
            print("A castigat 0")
            a_castigat_y = True

    ### Diagonala stanga sus dreapta jos
    if tabla[0][0] == tabla[1][1] == tabla[2][2] == "X":
            print("A castigat x")
            a_castigat_x = True
    elif tabla[0][0] == tabla[1][1] == tabla[2][2] == "0":
            print("A castigat 0")
            a_castigat_y = True

    ### Diagonala dreapta sus stanga jos
    elif tabla[2][0] == tabla[1][1] == tabla[0][2] == "X":
            print("A castigat x")
            a_castigat_x = True
    elif tabla[2][0] == tabla[1][1] == tabla[0][2] == "0":
            print("A castigat 0")
            a_castigat_y = True

    #### Verificari
    if este_terminat and a_castigat_x == a_castigat_y == False:
        print("Remiza")

    if any([este_terminat, a_castigat_x, a_castigat_y]):
        raspuns = input("Joc noul? DA/nu ")
        if raspuns == "DA":
            tabla =  [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            incepe_X = not incepe_X
            este_randul_lui_X = incepe_X
        else:
            break

        

 