import os
os.system ("clear || cls")

from dataclasses import dataclass


@dataclass

class Autor:
    nome: str
    biografia: str

@dataclass

class Livro:
    titulo: str
    ano: int
    autor: Autor
    def exibir_detalhes(self):
        print(f"Nome: {self.autor.nome}\nBiografia: {self.autor.biografia}\nTitulo: {self.titulo}\nAno: {self.ano}")

autor_instancia = Autor(
    nome = input("Nome do autor: "),
    biografia = input("Biografia: ")
)

biblioteca = Livro(
    titulo= input("Titulo do livro: "),
    ano= input("Ano do livro: "),
    autor= autor_instancia
)

os.system ("clear || cls")

biblioteca.exibir_detalhes()