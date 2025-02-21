import os
os.system ("clear")

#Front

print("""
==================MENU=======================|
Código|\tPrato    \t\tValor|
1     |\tLasanha  \t\t20,00|
3     |\tStrogonoff \t\t18,00|
4     |\tBife acebolado  \t15,00|
5     |\tPão com ovo \t\t5,00 |
=============================================|
      
""")


#Entrada de dados

nome = str(input("Digite seu nome: "))
opcao = str(input("Digte o codigo do produto: "))
import os
os.system ("clear")
#Saida de dados
import random
numero_pedido = random.randint (1,100)
print(f"Nome do cliente: {nome}")
print()
print(f"Seu codigo de fila é: {numero_pedido}")

match opcao:
    case "1":
        print("Seu prato é : Picanha 25,00")
    case "2":
        print("Seu prato é : Lasanha  20,00")
    case "3":
        print("Seu prato é : Strogonoff 18,00")
    case "4":
        print("Seu prato é : Bife acebolado 15,00")
    case "5":
        print("Seu prato é : Pão com ovo 5,00")  
    case _:
        print("Seu prato é : Opção ivalida")   
