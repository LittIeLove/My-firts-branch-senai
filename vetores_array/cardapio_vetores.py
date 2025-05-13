import os
os.system ("clear || cls")
from time import sleep

pratos = []
precos = []


def cardapio (cardapio):
    print("""
==================MENU=======================|
Código|\tPrato    \t\tValor|
1     |\tPicanha  \t\t25.00
2     |\tLasanha  \t\t20,00|
3     |\tStrogonoff \t\t18,00|
4     |\tBife acebolado  \t15,00|
5     |\tPão com ovo \t\t5,00 |
0     |\tSair \t\t\t0,00 |
=============================================|
      
""")

while True:
    cardapio(cardapio)
    sim_não = int(input("Deseja fazer um pedido ? (1 para sim) "))
    match sim_não:
        case 1:
            nome_prato = int(input("Digite o codigo do prato: "))
            if nome_prato == 1:
                pratos.append("Picanha 25.00")
                precos.append(25)
            elif nome_prato == 2:   
                pratos.append("Lasanha 20.00")
                precos.append(20)
            elif nome_prato == 3:
                pratos.append("Strogonoff 18.00")
                precos.append(18)
            elif nome_prato == 4:
                pratos.append("Bife acebolado 15.00")
                precos.append(15)
            elif nome_prato == 5:
                pratos.append("Pão com ovo 5.00")
                precos.append(5)
            else:
                print("Prato não encontrado. Tente novamente.")
                

        case 0:
            break
        case _:
            print("Opção inválida.\nTente novamente.")
            sleep (1)
    os.system ("clear || cls")

os.system ("clear || cls")
print("Pedido finalizado")
print(f"Pratos pedidos: {pratos}")
print(f"Total: {sum(precos)}")