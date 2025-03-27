import os
os.system ('clear || cls')
from time import sleep
pares = 0
par = 0
impar = 0
impares = 0
numeros = 0


while True:
    n = float(input("Digite os numeros pares e impares (Para encerrar digite o numero 0): "))
    if n  % 1 or n == 1:
        impar += 1
        impares += n
        numeros += n
    elif n == 0:
        os.system ("clear || cls")
        break
    

    else:
        par += 1
        pares += n
        numeros += n
if par == 0 and impar == 0:
    print("Total = (0)\nEncerrando...")
    sleep(2)
    os.system ("clear || cls")
    print("Obrigado por utilizar.")
    exit()

print("Resultados:")
print("\nQuantidade de números pares e impares: ")
print(f"par ({par}) e impar ({impar})")
print(f"A media total é ({ numeros / (par + impar)})")
if pares > 0:
    print(f"A média dos numeros pares ({pares / par})")
else:
    print("A média dos numeros pares (0)")


