import os
os.system ("clear || cls")
# Importa o decorador dataclass do módulo dataclasses
from dataclasses import dataclass

# Define a classe de dados Pessoa (igual ao exemplo anterior)
@dataclass
class Pessoa:
    """Representa uma pessoa com nome e idade."""
    nome: str
    idade: int

# Cria uma lista vazia para armazenar objetos Pessoa
lista_pessoas = []


# Loop para coletar dados do usuário
while True:
    os.system ("clear || cls")
    print("Digite os dados das pessoas. Digite 'sair' no nome para terminar.")
    # Pede o nome ao usuário
    nome_input = input("Digite o nome da pessoa: ")

    # Verifica se o usuário quer sair
    if nome_input.lower() == 'sair':
        break # Sai do loop se digitar 'sair'

    # Pede a idade ao usuário
    try:
        idade_input = int(input(f"Digite a idade de {nome_input}: "))
    except ValueError:
        # Trata caso o usuário digite algo que não seja um número para a idade
        print("Idade inválida. Por favor, digite um número.")
        continue # Volta para o início do loop para pedir os dados novamente

    # Cria uma nova instância da classe Pessoa com os dados informados
    nova_pessoa = Pessoa(nome=nome_input, idade=idade_input)

    # Adiciona a nova instância à lista
    lista_pessoas.append(nova_pessoa)

    print(f"Pessoa '{nome_input}' adicionada.")

# Após sair do loop, imprime a lista final de pessoas
os.system ("clear || cls")
print("\n--- Lista Final de Pessoas ---")
if not lista_pessoas:
    print("Nenhuma pessoa foi adicionada.")
else:
    for pessoa in lista_pessoas:
        print(f"- Nome: {pessoa.nome}, Idade: {pessoa.idade}")

