import os
os.system ("clear || cls")
from time import sleep

def contar_pares_impares():
    pares = 0
    impares = 0
    try:
        for i in range(6):
            numeros = int(input("Digite um número: "))
            if numeros % 2 == 0:
                pares += 1
            else:
                impares += 1
    except ValueError:
        os.system ("clear || cls")
        print("Foi identificado um digito incorreto ou a falta de digito.\nfaça novamente")
        sleep(1.5)
        exit()
    return pares, impares
 
quantidade_pares,quantidade_impares = contar_pares_impares()
os.system("clear || cls")   

print(f"\nQuantidade de pares: {quantidade_pares}")
print(f"Qunatidade de impares: {quantidade_impares}")

        