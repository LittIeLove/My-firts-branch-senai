import os
os.system ("clear || cls")
from time import sleep

def numeros(menos_mais):

    os.system ("clear || cls")

    if menos_mais > 0:
        print(f"O números {menos_mais} é positivo")
    elif menos_mais < 0:
        print(f"O números {menos_mais} é negativo")
    else:
        print("0 é neutro")

while True:
    try:
        input_usuario = input("Digite um valor (Digite S para encerrar): ")
        if input_usuario.upper() == "S":
            print("Obrigado por utilizar\nEncerrado")
            sleep(1)
            os.system ("clear || cls")
            break

        nu1 = float(input_usuario)
        numeros(nu1)
        
    except ValueError:
        os.system ("clear || cls")
        print("Valor invalido\nDigite outro valor")
        sleep(1)
        