import os
import time
os.system ("clear || cls") #LIMPANDO DADOS

#VARIAVEL PARA SOMA DOS DADOS
notasn = 0

#ENTRADA DE DADOS

for i in range(4):
    notas = float(input("Digite sua nota: "))
    notasn += notas

media = notasn / 4

os.system ("clear || cls")

#SAIDA DE DADOS
print("Calculando sua media...")
time.sleep(1)
os.system ("clear || cls")
if media >= 7:
    situacao = "APROVADO"

elif media >=5:
    situacao ="RECUPERAÇÃO"

else:
    situacao = "REPROVADO"


print(f"Sua media é : {media:.1f}")

print(".")
time.sleep(0.5)

print(".")
time.sleep(0.5)

print(".")
time.sleep(0.5)

os.system ("clear || cls")

print(f"Situação: {situacao}")

