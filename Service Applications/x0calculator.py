import random
        # 00 , 01,  02     10   11  12      20   21  22
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

    if este_randul_lui_X:
        alegere = input(f"Alegeti pozitia {printeaza_tabla(demo)}")
        print(alegere)
        while alegere not in [str(i) for i in range(1, 10)]:
            alegere = input(f"Alegeti pozitia {printeaza_tabla(demo)}")
        alegere = int(alegere)
        index_0 = (alegere-1) // 3 
        index_1 = (alegere-1) % 3

    else:

        if tabla[1][1] == " ":
             alegere = 5
        elif tabla[1][1] == "0" and ((tabla[0][0] == tabla[2][2] == "X") or (tabla[2][0] == tabla[0][2] == "X")):
            alegere = random.choice([2, 4, 6, 8])
        elif tabla[0][0] == " " or tabla[0][2] == " " or tabla[2][0] == " " or tabla[2][2] == " ":
            alegere = random.choice([1, 3, 7, 9])
        else:
            alegere = random.choice([2, 4, 6, 8])

        index_0 = (alegere-1) // 3 
        index_1 = (alegere-1) % 3

        ###################
        #### PERICOL
        ###
        ### Orizontala
        for i0 in range(3):
            if ((tabla[i0][0] == tabla[i0][1]  == "0") or (tabla[i0][0] == tabla[i0][1]  == "X"))  and tabla[i0][2] == " ":
                index_0 = i0
                index_1 = 2
            elif ((tabla[i0][0] == tabla[i0][2]  == "0") or (tabla[i0][0] == tabla[i0][2]  == "X")) and tabla[i0][1] == " ":
                index_0 = i0
                index_1 = 1
            elif ((tabla[i0][1] == tabla[i0][2]  == "0") or (tabla[i0][0] == tabla[i0][2]  == "X")) and tabla[i0][0] == " ":
                index_0 = i0
                index_1 = 0
                
        ## Verticala
        for i1 in range(3):
            if ((tabla[0][i1] == tabla[1][i1] == "0") or (tabla[0][i1] == tabla[1][i1] == "X")) and  tabla[2][i1] == " ":
                index_0 = 2
                index_1 = i1
            elif ((tabla[1][i1] == tabla[2][i1] == "0") or (tabla[1][i1] == tabla[2][i1] == "X")) and  tabla[0][i1] == " ":
                index_0 = 0
                index_1 = i1
            elif ((tabla[0][i1] == tabla[2][i1] == "0") or (tabla[0][i1] == tabla[2][i1] == "X")) and  tabla[1][i1] == " ":
                index_0 = 1
                index_1 = i1
        
        ## Diagona principala
        if ((tabla[0][0] == tabla[1][1] == "0") or (tabla[0][0] == tabla[1][1] == "X")) and  tabla[2][2] == " ":
             index_0 = 2 
             index_1 = 2
        elif ((tabla[0][0] == tabla[2][2] == "0") or (tabla[0][0] == tabla[2][2] == "X")) and   tabla[1][1] == " ":
             index_0 = 1 
             index_1 = 1
        elif ((tabla[1][1] == tabla[2][2] == "0") or (tabla[1][1] == tabla[2][2]  == "X")) and   tabla[0][0] == " ":
             index_0 = 0 
             index_1 = 0

         ## Diagona secundara
        if ((tabla[2][0] == tabla[1][1] == "0") or (tabla[2][0] == tabla[1][1] == "X")) and   tabla[0][2] == " ":
             index_0 = 0 
             index_1 = 2
        elif ((tabla[2][0] == tabla[0][2] == "0") or (tabla[2][0] == tabla[0][2] == "X")) and   tabla[1][1] == " ":
             index_0 = 1 
             index_1 = 1
        elif ((tabla[1][1] == tabla[0][2] == "0") or (tabla[1][1] == tabla[0][2] == "X")) and   tabla[2][0] == " ":
             index_0 = 2 
             index_1 = 0

        #### TERMINAT PERICOL
        ######################

    if tabla[index_0][index_1] not in ['X', '0']:
        tabla[index_0][index_1] = 'X' if este_randul_lui_X else '0'
        print(printeaza_tabla(tabla))
        este_randul_lui_X = not este_randul_lui_X
    # else:
        # print("Nu se poate asa ceva")


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

        

 