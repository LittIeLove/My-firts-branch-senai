# 1 LIMPANDO O TERMINAL
import os
os.system ("clear")

# 2 BANCO
login_cadastrado = "aluno"
senha_cadastrada = "123"

# ENTRADA DE DADOS
login =input("Digite seu login: ")
senha = input("Digite sua senha: ")

#SAIDA DE DADOS
if login_cadastrado == login and senha_cadastrada == senha:
    print ("Bem-Vindo")
else:
    print("Login ou senha inválidos")
