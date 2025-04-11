import os
os.system ("cls || clear")


numeros = []

par = 0
impar = 0
for i in range (6):
    n = float(input(f"Digite o {i + 1}ª: "))
    numeros.append(n)

for n in numeros:
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"Números pares e impares\nPares {par}\nImpares {impar}")



        