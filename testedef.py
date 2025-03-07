import os

def limpar_tela():
    os.system("clear")

def obter_valor_produto():
    while True:
        try:
            valor = float(input("Digite o valor do produto: "))
            if valor <= 0:
                print("O valor deve ser maior que zero 0! Tente novamente.\n")
            else:
                return valor
        except ValueError:
            print("Entrada inválida! DIgite apenas números. \n")
    
def obter_forma_pagamento():
    while True:
        try:
            forma =int[1,2]:
            if forma in [1,2]:
                return forma
            else:
                print("Opção inválida! Escolha 1 para debito ou 2 para crédito.\n")
            
        except ValueError:
            print("Entrada inválida! Digite apenas número.\n")


def obter_parcelas():
    while True:
        try:
            parcelas = int(input("Digite a quantidade de parcelas (1x até 6x): "))
            if 1 <= parcelas <= 6:
                return parcelas
            else:
                print("Número de ")