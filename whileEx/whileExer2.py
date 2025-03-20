import os   
os.system ("clear || cls")
from time import sleep


nota = float(input("Digite a sua nota: "))

while nota < 0 or nota >10:
    print(f"Nota invalida : (Media total de 1 até 10) \nNota incerida: {nota}")
    sleep(3)
    nota = float(input("Digite a sua nota: "))
    os.system ("cls || clear")

print(f"Sua nota é: {nota}")

