import os 
os.system ("clear")

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
print()
import os 
os.system ("clear")

print(f"Numeros informados: {n1} / {n2}")
print()
maior_numero = max(n1,n2)
menor_numero = min(n1,n2)
if maior_numero == menor_numero:
    print("Os numeros são iguais")

else:

    print(f"Maior numero: {maior_numero}")
    print(f"Menor_numero: {menor_numero}")
