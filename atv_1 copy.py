import os
os.system ("clear")
valor = float(input("Digite o valor do produto: "))
print("""
1 - A vista
2 - parcelado
""")


if valor == 0:
    print("Valor não pode ser cobrado!")

forma = int(input("escolha a forma de pagamento: "))
os.system ("clear")
if forma > 0 and forma < 2:
    debito = "Debito"
    debitod = valor * 0.1
    valorff = valor - debitod

else:
    print()

if forma == 2:
    credito = "Credito"

     
     

match forma:
    case 1:
        debitod = valor  * 0.1
        print (f"Valor do Produto: {valor}")
        print (f"Forma de pagamento: {debito}")
        print(f"Desconto de: {debitod:.2f}R$ ")
        print(f"Valor final: {valorff:.2f}")

    case 2:
        print("Digite o numero de parcelas (De 1x até 6x)")
        parcela = int(input("Parcelas: "))
        os.system ("clear")
        parcelas = valor / parcela
        print(f"Quantidade de parcelas: {parcela}")
        print(f"Valor do produto: {valor}")
        print(f"Forma de pagamento: {credito}")
        print(f"Valor da parcela: {parcelas:.2f}")
        print(f"Total a prazo: {valor}")
    case _:
        print("Forma invalida")








