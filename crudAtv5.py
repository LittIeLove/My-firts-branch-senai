import os
os.system ("clear || cls")

from dataclasses import dataclass

lista_funcionario = []
lista_clientes = []
QTD_FUNCIONARIOS = 3
QTD_CLIENTES = 3

@dataclass
class Funcionario:
    nome: str
    data_admissao: int
    matricula: int
    endereco: str

@dataclass
class Cliente:
    nome: str
    data_nascimento: int
    endereco: str

def cadastrar_funcionario():
    os.system("clear || cls")
    print("Cadastro de Funcionários:")
    for i in range (QTD_FUNCIONARIOS):
        nome = input(f"Digite o nome do funcionário {i+1}: ")
        data_admissao = int(input(f"Digite a data de admissão de {nome}: "))
        matricula = int(input(f"Digite a matrícula de {nome}: "))
        endereco = input(f"Digite o endereço de {nome}: ")
        funcionario = Funcionario(nome, data_admissao, matricula, endereco)
        lista_funcionario.append(funcionario)

def cadastrar_cliente():
    os.system("clear || cls")
    print("Cadastro de Clientes:")
    for i in range (QTD_CLIENTES):
        nome = input(f"Digite o nome do cliente {i+1}: ")
        data_nascimento = int(input(f"Digite a data de nascimento de {nome}: "))
        endereco = input(f"Digite o endereço de {nome}: ")
        cliente = Cliente(nome, data_nascimento, endereco)
        lista_clientes.append(cliente)

cadastrar_funcionario()
cadastrar_cliente()

arquivo_funcionarios = "Dados dos funcionarios.txt"
arquivo_clientes = "Dados dos clientes.txt"

os.system("clear || cls")

print("Salvando dados dos funcionários...")

def salvar_dados_funcionario():
    with open(arquivo_funcionarios, "a") as arquivo:
        for funcionario in lista_funcionario:
            arquivo.write(f"Nome: {funcionario.nome}\n")
            arquivo.write(f"Data de admissão: {funcionario.data_admissao}\n")
            arquivo.write(f"Matricula: {funcionario.matricula}\n")
            arquivo.write(f"Endereço: {funcionario.endereco}\n")
            arquivo.write("-"*20 + "\n")

    print("Dados dos funcionários salvos com sucesso!")
salvar_dados_funcionario()
print("\nSalvando dados dos clientes...")

def salvar_dados_cliente():
    with open (arquivo_clientes,"a") as arquivo:
        for cliente in lista_clientes:
            arquivo.write(f"Nome: {cliente.nome}\n")
            arquivo.write(f"Data de nascimento: {cliente.data_nascimento}\n")
            arquivo.write(f"Endereço: {cliente.endereco}\n")
            arquivo.write("-"*20 + "\n")
salvar_dados_cliente()
print("Dados dos clientes salvos com sucesso!")

def exibir_dados_funcionario():
    with open(arquivo_funcionarios, "r") as arquivo:
        linhas = arquivo.readlines()
        for linhas in linhas:
            print(linhas.strip())

def exibir_dados_cliente():           
    with open(arquivo_clientes, "r") as arquivo:
        linhas = arquivo.readlines()
        for linhas in linhas:
            print(linhas.strip())

exibir_dados_funcionario()
print("\n")
exibir_dados_cliente()