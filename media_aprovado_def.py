import os
os.system ("cls || clear")

# def somatorio():
#     nota = 0
#     for i in range(1,4):
#         nota += float(input(f"Digite {i}ª sua nota: "))
    
#     return nota / 3

# resultado = somatorio()

# print(f"Sua media é = {resultado}")

soma = 0

def calcular(soma):
    return soma / 2

for i in range (2):
    nota = float(input("DIgite uma nota:"))
    soma += nota
soma_final = calcular(soma)

if soma_final >= 7:
    print(f"Você está aprovado\nMedia{soma_final:.2f}")
    
else:
    print(f"Você esta reprovado\nMedia {soma_final:.2f}")


