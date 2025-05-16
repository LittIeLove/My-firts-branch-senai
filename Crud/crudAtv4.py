import os
os.system ("clear || cls")
from dataclasses import dataclass

QUANTIDADE_LIVROS = 3

lista_livros = []
@dataclass

class Ler_livro: #Classe para criar o livro
    nome: str
    autor: str
    categoria: str
    preco: float
    # def ler_dados_catalogo(self): #Método para ler os dados do livro
    #     print(f"Nome: {self.nome}")
    #     print(f"Autor: {self.autor}")
    #     print(f"Categoria: {self.categoria}")
    #     print(f"Preço: {self.preco}")


for i in range (QUANTIDADE_LIVROS): #Vai pedir os dados do livro
    livros = Ler_livro(
        input("Nome: "),
        input("Autor: "),
        input("Categoria: "),
        float(input("Preço: "))
    )
    lista_livros.append(livros)

os.system ("clear || cls")

# for Ler_livro in lista_livros: #Vai printar os dados do livro
#     Ler_livro.ler_dados_catalogo()
#     print("\n")
#     print("=========================================")

nome_arquivo = "livros.txt" #Nome do arquivo
#Criando o arquivo
print("Salvando Dados")
with open (nome_arquivo, "a") as arquivo:
    for livro in lista_livros:
        arquivo.write(f"Nome: {livro.nome}\n")
        arquivo.write(f"Autor: {livro.autor}\n")
        arquivo.write(f"Categoria: {livro.categoria}\n")
        arquivo.write(f"Preco: {livro.preco}\n")
        arquivo.write("-"*30 + "\n") # Adicionei uma quebra de linha aqui

print("Salvo com Sucesso.")

os.system ("clear || cls")
print("\nAcessando dados do arquivo")

try:
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linha.strip())
except FileNotFoundError:
    print("Arquivo não encontrado.")