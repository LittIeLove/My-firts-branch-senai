import os
os.system ("clear || cls")

numeros = []

def numero():
    for i in range(5):
        n = int(input("Digite um número: "))
        numeros.append(n)


def mostrando():
    os.system("clear || cls")
    for i in (numeros):
        if  i < 0:
            i = 0
        print(i)
numero()
mostrando()
