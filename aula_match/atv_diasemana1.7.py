import os
os.system ("clear")

#Mostrando opções

print(""" 
=================DIA=================
1 = Domingo
2 = segunda
3 = terça
4 = quarta
5 = quinta
6 = sexta
7 = sabado
      """)
#2 entrada de dados

n1 = float(input("Digite um numero da semana: "))

os.system ("clear")

print(""" 
=================DIA=================
1 = Domingo
2 = segunda
3 = terça
4 = quarta
5 = quinta
6 = sexta
7 = sabado
      """)
#3 saida de dados

match n1:
    case 1|7:
        resultado =("Fim de semana.")
    case 1|2|3|4|5|6:
        resultado = ("Dia Útil.")
    case _:
        resultado = ("Dia invalido")
    
print()
print(f"Resultado: {resultado}")


