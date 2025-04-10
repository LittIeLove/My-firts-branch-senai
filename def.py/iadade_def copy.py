import os
os.system ("clear || cls")

#Lembre o def é um codigo separado, para utilizaro tera de puxar o mesmo
def calcular_idade(data_nascimento):
    return 2025 - data_nascimento
    

data_nascimento = int(input("Digite o ano em que nasceu: "))

idade_resultante = calcular_idade(data_nascimento)
print(f"Se você nasceu em {data_nascimento} você tem {idade_resultante} anos.")
