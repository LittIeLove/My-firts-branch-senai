import os
os.system ("clear || cls")
from dataclasses import dataclass

QUANTIDADE_LIVROS = 3

lista_livros = []
@dataclass

class Ler_livro:
    nome: str
    autor: str
    categoria: str
    preco: float
    def ler_dados_catalogo(self):
        



for i in range (QUANTIDADE_LIVROS):
    livros = Ler_livro(
        input("Nome: "),
        input("Autor: "),
        input("Categoria"),
        input("Preço: ")
    )
    


