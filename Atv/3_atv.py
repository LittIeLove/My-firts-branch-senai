import os
os.system ("clear")
#Entrada de dados
#Ctrl seleciona palavras para edição

n1 = float(input("Digte sua  primera nota: "))
print()
n2 = float(input("Digte sua  segunda nota: "))
print()
n3 = float(input("Digte sua  terceira nota: "))
print()


media = (n1 + n2 + n3) / 3

#saida de dados

if media < 7:
    resultado = "Reprovado"
elif media >= 7:
    resultado = "Aprovado"

print(f"Media: {media}")
print(f"Resultado: {resultado}")

    


