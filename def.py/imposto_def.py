import os
os.system ("clear || cls")
from time import sleep

def imposto():
    try:
        valor = float(input("Insira o valor do produto: "))
        if valor == 0:
            print ("Nenhum valor adicionado")
        elif valor < 100:
            inflação = valor * 0.1
        else:
            inflação = valor * 0.2
    except ValueError:
        print("Apenas números.")
        sleep(1)
        exit()


    valor_final = valor + inflação
    return valor,inflação,valor_final


valor_adicionado,impostos,valor_pagamento = imposto()
print(f"O produto de valor {valor_adicionado} obteve uma taxa de {impostos}\nSeu valor final é {valor_pagamento}")