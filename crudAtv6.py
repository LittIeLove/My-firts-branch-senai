import os
os.system ("clear || cls")
from dataclasses import dataclass
from time import sleep
lista_funcionarios = []

@dataclass
class Funcionario:
    nome:  str
    data_admissao: str
    cpf: str
    funcao: str


def add_funcionario(lista):

    funcionario = Funcionario(
        nome = input("Digite o nome: "),
        data_admissao= input("Digite a data de admissão: "),
        cpf = input("Digite o cpf: "),
        funcao = input("Digite a função: ")
    )
    lista_funcionarios.append(funcionario)
    print(f"\n{funcionario.nome} adicionado com sucesso.")

def mostrar_funcionarios(lista):
    if not lista:
        print("\nA lista está vazia")
        return
    print("\n= Lista de funcionários =")
    for funcionario in lista_funcionarios:
        print(f"- Nome: {funcionario.nome}, Data de admissão: {funcionario.data_admissao}, CPF: {funcionario.cpf}, Função: {funcionario.funcao}")

def atualizar_funcionario(lista):
    if not lista:
        print("\nA lista está vazia")
        return
    mostrar_funcionarios(lista)
    nome_antigo = input("Digite o nome do funcionário que deseja atualizar: ")
    for funcionario in lista_funcionarios:
        if funcionario.nome == nome_antigo:
            funcionario.nome = input("Digite o novo nome: ")
            funcionario.data_admissao = input("Digite a nova data de admissão: ")
            funcionario.cpf = input("Digite o novo cpf: ")
            funcionario.funcao = input("Digite a nova função: ")
            print(f"\n{funcionario.nome} atualizado com sucesso.")
            return
        else:
            print(f"\nFuncionário {nome_antigo} não encontrado.")
            return
    

def excluir_funcionario(lista):
    if not lista:
        print("\nA lista está vazia")
        return
    mostrar_funcionarios(lista)
    nome = input("Digite o nome do funcionário que deseja excluir: ")

    for funcionario in lista_funcionarios:
        if funcionario.nome == nome:
            lista.remove(funcionario)
            print(f"\n{funcionario.nome} excluído com sucesso.")
            return
    print(f"\nFuncionário {nome} não encontrado.")

def painel():
    try:
        while True:   
            print("1 - Adicionar")
            print("2 - mostrar")
            print("3 - atualizar")
            print("4 - excluir")
            print("5 - sair")
            opcao = int(input("Digite uma das opções acima: "))
            match opcao:
                case 1:
                    os.system ("clear || cls")
                    add_funcionario(lista_funcionarios)
                case 2:
                    os.system ("clear || cls")
                    mostrar_funcionarios(lista_funcionarios)
                case 3:
                    os.system ("clear || cls")
                    atualizar_funcionario(lista_funcionarios)
                case 4:
                    os.system ("clear || cls")
                    excluir_funcionario(lista_funcionarios)
                case 5:
                    os.system ("clear || cls")
                    print("\nSaindo do programa.")
                    sleep(2)
                    break
                case _:
                    os.system ("clear || cls")
                    print("\nOpção inválida.\nTente novamente.")
    except ValueError:
        print("Digite apenas números.")
painel()