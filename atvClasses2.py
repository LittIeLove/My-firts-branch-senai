import os
os.system ("clear || cls")

from dataclasses import dataclass
@dataclass

class Endereco:
    logradouro: str
    numero: int

@dataclass

class pessoa:
    #Atributos
    nome: str
    idade: int
    endereco: Endereco
    
    #Metódos
    def exibir_dados(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nEndereço: {self.endereco.logradouro}\nNúmero: {self.endereco.numero}")


#Aplicando caracteristicas da classe.

endereco1 = Endereco("Rua A", 47)
pessoa1 = pessoa("Marta", 41, endereco1)
pessoa1.exibir_dados()
print()
endereco2 = Endereco("Rua B", 46)
pessoa2 = pessoa("Martin", 42, endereco2)
pessoa2.exibir_dados()


