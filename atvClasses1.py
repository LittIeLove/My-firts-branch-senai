import os
os.system ("clear || cls")

from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

lista_pessoas = []

while True:
    nome_input = input("Digite 'sair' para encerrar.\nDigite o nome: ")
    if nome_input.lower() == "sair":
        break
    try:
        idade_input = int(input("Digite sua idade: "))
        peso_input = float(input("Digite seu peso: "))
        altura_input = float(input("Digite sua altura: "))
    except ValueError:
        print("Alguma das informações está incorreta.")
    nova_pessoa = Pessoa(nome= nome_input, idade= idade_input, peso= peso_input,altura= altura_input)
    lista_pessoas.append(nova_pessoa)
print("Lista das informações.")

os.system ("clear || cls")
for Pessoa in lista_pessoas:
    print(f"Nome: {Pessoa.nome}\nIdade: {Pessoa.idade}\nPeso: {Pessoa.peso}\nAltura: {Pessoa.altura}")
    print("-------------------")