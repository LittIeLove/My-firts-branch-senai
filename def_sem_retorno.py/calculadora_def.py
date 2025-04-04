import os
os.system ("clear || cls")
from time import sleep
def mais (a,b):
    return a + b
def menos (a,b):
    return a - b
def multi(a,b):
    return a * b
def divisao(a,b):
    if divisao == 0:
        return "Erro ! Divisão por 0"
    return a / b



def caculadora ():
    while True:
        try:  
            print("""
        1 - soma
        2 - subtração
        3 - multiplicação
        4 - divisão
        5 - sair""")
            operação =int(input("Digite a operação: "))
        except ValueError:
            print("Operação invalida.\nTente novamente.")
            sleep(1)
        if operação == 5:
            print("Encerrando o Programa.")
            sleep(1)
        
        try:
            n1 = float(input("Digite o 1ª numero: "))
            n2 = float(input("Digite o 2ª numero: "))

        except ValueError:
            print("Apenas número.")
            sleep(1)
        if operação == 1:
            os.system ("clear || cls")
            print(f"{n1} + {n2} = {mais(n1,n2)}")
        elif operação == 2:
            os.system ("clear || cls")
            print(f"{n1} - {n2} = {menos(n1,n2)}")
        elif operação == 3: 
            os.system ("clear || cls")
            print(f"{n1} * {n2} = {multi(n1,n2)}")
        elif operação == 4:
            os.system ("clear || cls")
            print(f"{n1} / {n2} = {divisao(n1,n2)}")
        else:
            os.system ("clear || cls")
            print("Operação inválida")
            sleep(1)
            
caculadora()
