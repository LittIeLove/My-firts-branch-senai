import os
os.system ("clear || cls")


def tabuada(numero):
    os.system ("clear || cls")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

n1 = int(input("Digite o numero para mostrar sua tabuada de 1 até 10: "))

tabuada(n1)