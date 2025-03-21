import os
os.system ("clear || cls")
from time import sleep

print("""
==================MENU=======================|
Código|\tPrato    \t\tValor|
1     |\tPicanha  \t\t25.00
2     |\tLasanha  \t\t20,00|
3     |\tStrogonoff \t\t18,00|
4     |\tBife acebolado  \t15,00|
5     |\tPão com ovo \t\t5,00 |
=============================================|
      
""")

prato = int(input("Digite o numero do prato: "))

#Repetição 1 + Entrada de Dados 1
while True:
    if prato == 1:
        pedido = "Picanha"
        preco = 25
        pedir = int(input("\nGostaria de mais um prato (1 para sim \ Qualquer outro Nª para não) ? "))
        nome = "Picanha 25.00/"
        break
    elif prato == 2:
        pedido = "Lasanha"
        preco = 20
        pedir = int(input("\nGostaria de mais um prato (1 para sim \ Qualquer outro Nª para não) ? "))
        nome = "Lasanha 20.00/"
        break
    elif prato == 3:
        pedido = "Strogonoff"
        preco = 18
        pedir = int(input("\nGostaria de mais um prato (1 para sim \ Qualquer outro Nª para não) ? "))

        nome = "Strogonoff/"
        break
    elif prato == 4:
        pedido = "Bife acebolado/"
        preco = 15
        pedir = int(input("\nGostaria de mais um prato (1 para sim \ Qualquer outro Nª para não) ? "))
        nome = "Bife acebolado 15.00/"

        break
    elif prato == 5:
        pedido = "Pão com Ovo"
        preco = 5
        pedir = int(input("\nGostaria de mais um prato (1 para sim \ Qualquer outro Nª para não) ? "))
        nome = "Pão com Ovo 5.00/"

        break
    else:
        os.system ("clear || cls")
        print("""
==================MENU=======================|
Código|\tPrato    \t\tValor|
1     |\tPicanha  \t\t25.00
2     |\tLasanha  \t\t20,00|
3     |\tStrogonoff \t\t18,00|
4     |\tBife acebolado  \t15,00|
5     |\tPão com ovo \t\t5,00 |
=============================================|
      
""")
        print("Numero invalido")
        print("Repita o pedido")
        prato = int(input("Digite o numero do prato: "))



#REPETIÇÂO 2 + Entrada de Dados 2

while pedir == 1:
    i = 1
    os.system ("clear || cls")
    print("""
==================MENU=======================|
Código|\tPrato    \t\tValor|
1     |\tPicanha  \t\t25.00
2     |\tLasanha  \t\t20,00|
3     |\tStrogonoff \t\t18,00|
4     |\tBife acebolado  \t15,00|
5     |\tPão com ovo \t\t5,00 |
=============================================|
      
""")
    prato = int(input("Digite o numero do prato: "))
    if prato == 1:
        pedido = "Picanha"
        preco += 25
        pedir = int(input("Gostaria de mais um prato (1 Para sim \ Qualquer outro Nª para não) ? "))
        nome += "Picanha 25.00/"
    elif prato == 2:
        pedido = "Lasanha"
        preco += 20
        pedir = int(input("Gostaria de mais um prato (1 para sim \ Quaquer outro Nª para não) ? "))
        nome += "Lasanha 20.00/"
    elif prato == 3:
        pedido = "Strogonoff"
        preco += 18
        pedir = int(input("Gostaria de mais um prato (1 para sim \ Quaquer outro Nª para não) ? "))
        nome += "Strogonoff"
    elif prato == 4:
        pedido = "Bife acebolado"
        preco += 15
        pedir = int(input("Gostaria de mais um prato (1 para sim \ Quaquer outro Nª para não) ? "))
        nome += "Bife acebolado 15.00/"
    elif prato == 5:
        pedido = "Pão com Ovo"
        preco += 5
        pedir = int(input("Gostaria de mais um prato (1 para sim \ Quaquer outro Nª para não) ? "))
        nome += "Pão com Ovo 5.00/"
    else:
        os.system ("clear || cls")
        print("""
==================MENU=======================|
Código|\tPrato    \t\tValor|
1     |\tPicanha  \t\t25.00
2     |\tLasanha  \t\t20,00|
3     |\tStrogonoff \t\t18,00|
4     |\tBife acebolado  \t15,00|
5     |\tPão com ovo \t\t5,00 |
=============================================|
      
""")
        i += 1
        print(f"Prato invalido\nRefaça o pedido\n{i}ª Tentativa ")
        sleep(2)


valorg = preco * 0.1
gorjeta = int(input(f"Gostaria de pargar a gorjeta de 10% ? Valor ({valorg:.2f})\nsim(1) não(2): " ))

#Saida de Dados

while True:
    if gorjeta == 1:
        os.system ("clear || cls")
        print(f"Valor da compra = {preco + valorg:.2f}\nPratos:\n({nome})\nObrigado pela compra!")
        break

    elif gorjeta == 2:
        os.system ("clear || cls")
        print(f"Valor da compra = {preco:.2f}\nPratos:\n({nome})\n\nObrigado pela compra!")
        break

    else:
        os.system ("clear || cls")
        print("Ivalido\nRepita")
        int(input(f"Gostaria de pargar a gorjeta de 10% ? Valor ({valorg:.2f})\nsim(1) não(2): " ))





    



