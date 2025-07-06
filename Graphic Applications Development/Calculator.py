
from tkinter import *

window = Tk()

cifre_butoane = []

calcul = ""
operand_anterior = ""
semn = ""

def apasa_tasta(nr):
    global calcul, calcul_var
    print(f"Tasta {nr} a fost apasata")
    if calcul_var.get() == "0":
        calcul = str(nr)
    else:
        calcul += str(nr)
    print(f"calcul: {calcul }")
    calcul_var.set(calcul)

# lambda x
calcul_var = StringVar(value="0")
rez_lb = Label(window, textvariable = calcul_var)
rez_lb.grid(row=0, column=0, columnspan=3)
row_shift = 1

for index_j, j in enumerate((7, 4, 1)):
    for i in range(j, j+3):
        buton = Button(window, text=f"{i}", command= lambda x=i: apasa_tasta(x))
        buton.grid(row=index_j + row_shift, column=i-j)

i=0
buton = Button(window, text=f"{i}", command= lambda x=i: apasa_tasta(x))
buton.grid(row=3 + row_shift, column=0, columnspan=2, sticky = W+E)
i = "."
buton = Button(window, text=f"{i}", command= lambda x=i: apasa_tasta(x))
buton.grid(row=3 + row_shift, column=2)


def calculeaza(apasat):
    ## global operand_anterior...
    global calcul, calcul_var, semn, operand_anterior
    operand_anterior = calcul 
    calcul = "" 
    semn = apasat
    calcul_var.set(0)

def afiseaza_rezultatul():
    global operand_anterior, semn, calcul
    print("operand_anterior:", operand_anterior)
    print("semn:", semn)
    print("calcul:", calcul)
    rezultat = eval(f"{(operand_anterior)}{semn}{(calcul)}")
    calcul = rezultat
    operand_anterior = calcul
    calcul_var.set(rezultat)

for index, semn in enumerate(["/", "*", "-", "+"]):
    ## x = semn si nu i
    buton = Button(window, text=f"{semn}", command= lambda x=semn: calculeaza(x))
    buton.grid(row=index, column=3)

buton = Button(window, text=f"=", command=  afiseaza_rezultatul)
buton.grid(row=index + 1, column=3)



window.mainloop()



