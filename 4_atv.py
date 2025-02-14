import os
os.system ("clear")

n1= float(input("Digite o primeiro numero: "))
n2= float(input("Digite o segundo numero: "))

media = (n1 + n2) /2
soma = n1+n2
produto = n1 * n2

print (f"A media é: {media}")
print (f"A soma é: {soma}")
print (f"o produto é: {produto}")

maior_numero= max(n1,n2)
menor_numero= min(n1,n2)
print()
print(f"soma: {soma}")
print(f"media: {media}")
print(f"Produto: {produto}")
print(f"Maior numero: {maior_numero}")
print(f"Menor numero:{menor_numero}")

