import os
os.system ("clear || cls")

from dataclasses import dataclass
@dataclass

class Carro:
    marca: str
    modelo: str
    categoria: str
    preco: float

QUANTIDADE = 2


with open ("carros.txt", "w") as arquivo:
    for carros in range (QUANTIDADE):
        carros = Carro(
            marca = input("Marca do carro: "),
            modelo= input("Modelo: "),
            categoria= input("categoria: "),
            preco= input("Preço: ")
                    )
        arquivo.write (f"Marca: {carros.marca}\nModelo: {carros.modelo}\nCategoria: {carros.categoria}\nPreço: {carros.preco}\n----------------\n")
