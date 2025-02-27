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

n1= str(input("Digite o numero correspondente ao dia da semana: "))

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

match n1:
    case "1":
        print("Domingo - Final de semana")
    case "2":
        print("Segunda - Dia útil")
    case "3":
        print("Terça - Dia útil")
    case "4":
        print("Quarta - Dia útil")
    case "5":
        print("Quinta - Dia útil")
    case "6":
        print("Sexta - Dia útil")
    case "7":
        print("Sabado - final de semana")
    case _:
        print("Dia Invalido")
    


