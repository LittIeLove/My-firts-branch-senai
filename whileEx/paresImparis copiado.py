import os
os.system ('clear || cls')
from time import sleep
pares = 0
qtd_impares = 0
soma_pares = 0
soma_total = 0
total_numeros = 0

while True:
    numero = int(input("digite os números: "))
    if numero == 0:
        break
    if not numero:
        print("Nenhum número foi lido.")

total_numeros += 1
soma_total += numero

if numero % 2 == 0:
    pares += 1
    soma_pares += numero

else:
    qtd_impares += 1

if total_numeros == 0:
    print("Nenhum numero lido.")

media = soma_total / total_numeros

os.system ("clear || cls")

print("------------resultado------------")
sleep(2)
print(f"A quantidade de números pares é ({pares}) e impar ({qtd_impares})")
print(f"Media dos números pare ({soma_pares / pares})")
print(f"A media total é ({media})")

