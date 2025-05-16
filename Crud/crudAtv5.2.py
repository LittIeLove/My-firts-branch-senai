import os
os.system ("clear || cls")
from time import sleep
from dataclasses import dataclass

lista_funcionario = []
lista_clientes = []
QTD_FUNCIONARIOS = 1
QTD_CLIENTES = 1

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

def salvar_funcionarios(lista):
    nome_arquivo = "dados_funcionarios.csv"
    with open(nome_arquivo, "a") as arquivo_funcionarios:
        for funcionario in lista:
            arquivo_funcionarios.write(f"{funcionario.nome}, {funcionario.data_admissao}, {funcionario.matricula}, {funcionario.endereco}\n")
    
    print("Salvando dados dos funcionários...")

def salvar_clientes(lista):
    nome_arquivo = "dados_clientes.csv"
    with open(nome_arquivo, "a") as arquivo_funcionarios:
        for cliente in lista:
            arquivo_funcionarios.write(f"{cliente.nome}, {cliente.data_nascimento}, {cliente.endereco}\n")
    
    print("Salvando dados dos clientes...")


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
salvar_funcionarios(lista_funcionario)
sleep(1)
salvar_clientes(lista_clientes)
sleep(1)

os.system("clear || cls")
