import os

os.system("clear")

print("Olá,mundo")

#solicitar dados para o usuario
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
numero_1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
soma = int (numero_1 + n2)
#Exibindo dados
print(f"nome: {nome}")
print(f"idade: {idade}")
print(f"altura: {altura}")
print(f"Soma dos 2 numeros: {numero_1 + n2}")
print(f"Subtração dos 2 numeros: {numero_1 - n2}")


