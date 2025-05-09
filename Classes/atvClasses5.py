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
        print(f"Nome: {self.autor}\nTitulo: {self.titulo}\nAno: {self.ano}")

autor = Autor(
    nome = "Rogerio",
    biografia = "Rogério Ceni (Pato Branco, 22 de janeiro de 1973) é um treinador e ex-futebolista brasileiro que atuava como goleiro. Atualmente comanda o Bahia."
)

biblioteca = Livro(
    titulo = "O goleiro que batia falta",
    ano = 2025,
    autor = autor.nome
)
biblioteca.exibir_detalhes()