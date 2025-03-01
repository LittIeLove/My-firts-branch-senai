import os

os.system("clear")

# Entrada do valor do produto
valor = float(input("Digite o valor do produto: "))

# Opções de pagamento
print("""
1 - À vista (10% de desconto)
2 - Parcelado (Até 6x sem juros)
""")

forma = int(input("Escolha a forma de pagamento: "))
os.system("clear")

if forma == 1:
    # Pagamento à vista com 10% de desconto
    debito = "Débito"
    desconto = valor * 0.1
    valor_final = valor - desconto
    print(f"Valor do Produto: {valor}R$")
    print(f"Forma de pagamento: {debito}")
    print(f"Desconto: {desconto:.2f}R$")
    print(f"Valor final: {valor_final:.2f}R$")
    
elif forma == 2:
    # Pagamento parcelado
    print("Digite o número de parcelas (1x até 6x):")
    parcela = int(input("Parcelas: "))

    if 1 <= parcela <= 6:
        os.system("clear")
        valor_parcela = valor / parcela
        print(f"Quantidade de parcelas: {parcela}x")
        print(f"Valor do produto: {valor:.2f}R$")
        print(f"Forma de pagamento: Crédito")
        print(f"Valor da parcela: {valor_parcela:.2f}R$")
        print(f"Total a prazo: {valor:.2f}R$")
    else:
        print("Número de parcelas inválido! Escolha entre 1 e 6.")
else:
    print("Forma de pagamento inválida!")

