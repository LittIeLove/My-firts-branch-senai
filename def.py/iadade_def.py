import os
os.system ("clear || cls")

def data_nascimento():
    ano = int(input("Digite o ano em que nasceu: "))
    idade = 2025 - ano
    return ano,idade

ano_incerido,idade_resultante = data_nascimento()

os.system ("clear || cls")
print(f"Se você nasceu em {ano_incerido} você tera {idade_resultante} anos.")