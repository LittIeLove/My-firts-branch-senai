import os
os.system ("clear || cls")


numeros = []

def max_min(numeros):
    for i,n in enumerate(numeros , start = 1):
        print(f"{i}ª Números adicionado : {n} ")

    return f"O maior número é {max(numeros)} e o menor {min(numeros)}"
    
for i in range(1,6):
    numero = int(input("Digite um número para adicionalo: "))
    numeros.append(numero)


os.system ("clear || cls ")
lista = max_min(numeros)
print(lista)
    