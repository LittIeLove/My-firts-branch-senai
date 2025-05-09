import os
os.system ("clear || cls")

from dataclasses import dataclass
@dataclass

class Cliente:
    nome: str
    email: str
    telefone: str

lista_clientes = [] #Criando uma lista para adicionar clientes.

QUANTIDADE_DE_CLIENTE = 2

print("Informe os dados do usuario: ")

for i in range(QUANTIDADE_DE_CLIENTES):
    cliente = Cliente(
        nome = input("Nome: "),
        email = input("Email: "),
        telefone= input("Telefone: ")
    )
    lista_clentes.append(cliente)

print("Exibindo dados...")

for cliente in lista_clientes:
        print(f"Nome: {cliente.nome} ")
        print(f"Email:{cliente.email} ")
        print(f"Telefone: {cliente.telefone} ")
        print()
