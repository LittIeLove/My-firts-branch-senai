import os
os.system ("clear")

numero_maça = int(input("Quantas maçãs você quer ?: "))
import os
os.system ("clear")

print(f"Numero de maçãs: {numero_maça} ")
print()
if numero_maça < 12:
   numero_maça =  numero_maça * 1.30
   print(f"Valor total: {numero_maça:.2f}")

else:
    numero_maça = numero_maça * 1.0

    print(f"Valor total: {numero_maça:.2f}")
print()

if numero_maça > 0:
    print("Obrigado pela compra!")

else:
    print("Sai pobre!")

