import os
os.system ("clear || cls")
from time import sleep

def imposto():
    try:
        valor = float(input("Insira o valor do produto: "))
        if valor == 0:
            print ("Nenhum valor adicionado")
        elif valor < 100:
            inflação = valor * 1.1
        else:
            inflação = valor * 1.2
    except ValueError:
        print("Apenas números.")
        sleep(1)
        exit()


    return inflação


impostos = imposto()
print(f"O valor final do Produto é {impostos:.2f} ")