import os
os.system ("cls || clear")


numeros = []

def par_impar (numeros):
    par = 0
    impar = 0

    for numero in range(numeros):
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
    return par, impar

print("===Lista de números===")
def adcionando(numeros):
    for i in range (6):
        n = float(input(f"Digite {i + 1}ª : "))
        numeros.append(n)

adcionando(numeros)

for i,par_impares in enumerate(numeros, start=1):
    if par_impares % 2 == 0:
        print(f"{i}ª {par_impares} = Par ")
    else:
        print(f"{i}ª {par_impares} = Impar ")



        


    

        