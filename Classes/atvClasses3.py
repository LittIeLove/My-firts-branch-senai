import os
os.system ("clear || cls")

from dataclasses import dataclass
@dataclass

class Endereco:
    logradouro: str
    cidade: str
    numero: int

@dataclass

class pessoa:
    #Atributos
    nome: str
    email: str
    endereco: Endereco
    
    #Metódos
    def exibir_dados(self):
        print(f"Nome: {self.nome}\nEmail: {self.email}\nEndereço: {self.endereco.logradouro}\nCidade: {self.endereco.cidade}\nNúmero: {self.endereco.numero}")


#Aplicando caracteristicas da classe.

endereco1 = Endereco("Rua A", "Salvador",47)
pessoa1 = pessoa("Marta", "breno@", endereco1)
pessoa1.exibir_dados()
print()
endereco2 = Endereco("Rua B","salvador", 46)
pessoa2 = pessoa("Martin", "brenda@", endereco2)
pessoa2.exibir_dados()


