import os
os.system ("clear || cls")
from time import sleep

login = "breno"
senha = "123"

while True:
    loginu = str(input("DIgite seu login: ")).lower()
    senhau = str(input("Digite sua senha: "))
    if login == loginu and senha == senhau:
        sleep(1)

        print ("Entrada autorizada.")
        break
    else:
        print("Tente novamente!")


