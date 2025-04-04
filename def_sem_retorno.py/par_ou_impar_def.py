import os
os.system ("clear || cls")

def numeros(par_impar):
    par = 0
    impar = 0
    if par_impar == 0:
        exit()
    elif par_impar % 2 == 0:
        print(f"O numero {par_impar} é par")

    elif par_impar % 2 == 1:
        print(f"O numero {par_impar} é impar")


while True:
    try:
        nu1 = int(input("Digite um número (Digite o numero (0) para encerrar): "))
        numeros(nu1)
    except ValueError:
        print("Valor invalido")
