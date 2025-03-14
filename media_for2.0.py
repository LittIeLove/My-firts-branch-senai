import os
import time #PARA COMANDO "timer"
os.system ("clear || cls") #LIMPANDO DADOS

#VARIAVEL PARA SOMA DOS DADOS
notasn = 0

#ENTRADA DE DADOS

for i in range(3):
    notas = float(input("Digite sua nota: "))
    notasn += notas

media = notasn / 3

os.system ("clear || cls")

#PROCESSAMENTO

print("Calculando sua media...")
time.sleep(1.5)
os.system ("clear || cls")
if media >= 7:
    situacao = "APROVADO"

elif media >=4:
    situacao = "RECUPERAÇÃO"

elif media < 4:
    situacao = "REPROVADO"

else:
    print("Invalido")

#SAIDA DE DADOS

print(".")
time.sleep(0.5)

print(".")
time.sleep(0.5)

print(".")
time.sleep(0.5)

os.system ("clear || cls")

print(f"Sua media é : {media:.1f}")
print(f"Situação: {situacao}")

