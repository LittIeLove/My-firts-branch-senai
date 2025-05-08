import os
os.system ("clear || cls")

from dataclasses import dataclass
@dataclass

class pessoa:
    nome: str
    idade: int

pessoa1 = pessoa ("Bob", 30)
pessoa2 = pessoa ("Breno", 21)

print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade} ")
print()
print(f"Nome: {pessoa2.nome}\nIdade: {pessoa2.idade} ")