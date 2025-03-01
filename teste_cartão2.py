import os

def limpar_tela():
    os.system("clear")

def obter_valor_produto():
    while True:
        try:
            valor = float(input("Digite o valor do produto: "))
            if valor <= 0:
                print("O valor deve ser maior que 0! Tente novamente.\n")
            else:
                return valor
        except ValueError:
            print("Entrada inválida! Digite apenas números.\n")

def obter_forma_pagamento():
    while True:
        try:
            forma = int(input("Escolha a forma de pagamento: "))
            if forma in [1, 2]:
                return forma
            else:
                print("Opção inválida! Escolha 1 para débito ou 2 para crédito.\n")
        except ValueError:
            print("Entrada inválida! Digite apenas números.\n")

def obter_parcelas():
    while True:
        try:
            parcelas = int(input("Digite o número de parcelas (1x até 6x): "))
            if 1 <= parcelas <= 6:
                return parcelas
            else:
                print("Número de parcelas inválido! Escolha entre 1 e 6.\n")
        except ValueError:
            print("Entrada inválida! Digite um número entre 1 e 6.\n")

# Início do programa
limpar_tela()
valor = obter_valor_produto()

# Exibe opções de pagamento
print("""
1 - À vista (10% de desconto)
2 - Parcelado (Até 6x sem juros)
""")

forma = obter_forma_pagamento()
limpar_tela()

if forma == 1:
    # Pagamento à vista com 10% de desconto
    desconto = valor * 0.1
    valor_final = valor - desconto
    print(f"Valor do Produto: {valor:.2f} R$")
    print(f"Forma de pagamento: Débito")
    print(f"Desconto: {desconto:.2f} R$")
    print(f"Valor final: {valor_final:.2f} R$")

elif forma == 2:
    # Pagamento parcelado
    parcelas = obter_parcelas()
    limpar_tela()
    valor_parcela = valor / parcelas
    print(f"Quantidade de parcelas: {parcelas}x")
    print(f"Valor do produto: {valor:.2f} R$")
    print(f"Forma de pagamento: Crédito")
    print(f"Valor da parcela: {valor_parcela:.2f} R$")
    print(f"Total a prazo: {valor:.2f} R$")
