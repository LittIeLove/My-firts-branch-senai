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

for i in range(QUANTIDADE_DE_CLIENTE):
    cliente = Cliente(
        nome = input("Nome: "),
        email = input("Email: "),
        telefone= input("Telefone: ")
    )
    lista_clientes.append(cliente)

print("Exibindo dados...")

for cliente in lista_clientes:
        print(f"Nome: {cliente.nome} ")
        print(f"Email:{cliente.email} ")
        print(f"Telefone: {cliente.telefone} ")
        print()

#Texto que você quer salvar

print("Salvando os dados dos clientes =")
nome_arquivo = "dados_cliente.txt"

with open (nome_arquivo, "a") as arquivo:
     for cliente in lista_clientes:
          arquivo.write(f"{cliente.nome}, {cliente.email}, {cliente.telefone}\n")
          

#Abre o arquivo (ou cria se não existir) no modo de escrita ("w")

print("O texto foi salvo com sucesso no arquivo meu_arquivo.txt")
