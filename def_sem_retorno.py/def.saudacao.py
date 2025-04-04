import os
os.system ("clear || cls")

#Função sem retorno.
def saudacao(nome):
    print (f"Olá {nome}! Bem-vindo(a) ao curso de DS!")

nome_visitante = "Marta"
saudacao(nome_visitante) #Chamando a função

def diciplina(ds):
    print(f"A diciplina {ds} faz parte do curso de DS")
ds2 = str(input("\nDigite uma materia que faça parte de DS: "))
diciplina(ds2)
