import os 
os.system ("clear")
#2 - Entrada de dados
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

print()
import os 
os.system ("clear")
#Saida de dados
print(f"Numeros informados: {n1} / {n2} / {n3}")
print()
maior_numero = max(n1,n2,n3)
menor_numero = min(n1,n2,n3)
if n1 == n2 and n3 == n1:
    print("Os numeros tem o mesmo valor")

else:
    print(f"Maior numero: {maior_numero}")
    print(f"Menor_numero: {menor_numero}")
