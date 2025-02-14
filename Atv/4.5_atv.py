import os
os.system ("clear")
#entradad de dados
n1 = float(input("Digite o primeiro numero"))
n2 = float(input("Digite o segundo numero"))

soma= n1 + n2
media = (n1+n2)/2
produto = n1*n2

if n1 < n2:
    maior_numero = n2
    menor_numero = n1

else:
    maior_numero = n1
    menor_numero = n2
print(f"A soma é: {soma}")
print(f"O produto é: {produto}")
print(f"A media é: {media}")

if maior_numero == menor_numero:
    print("São iguais")

