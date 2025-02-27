import os
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

if n1 > 1 and n1 < 7:
    print("Dia Útil")

elif n1 == 1 or n1 == 7:
    print ("Final de semana")

else:
    print("invalido")


   
    