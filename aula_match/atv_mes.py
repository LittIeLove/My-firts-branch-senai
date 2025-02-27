import os
os.system ("clear")

#Mostrando opções

print(""" 
=================Mês=================
1 = janeiro      |   8 = agosto
3 = março        |   9 = Setembro
4 = Abril        |   10 = outubro
5 = Maio         |   11 = Novembro
6 = Junho        |   12 = Dezembro
      
      """)
#2 entrada de dados

n1 = str(input("Digite um numero do mês: "))

os.system ("clear")

print(""" 
=================Mês=================
1 = janeiro      |   8 = agosto
3 = março        |   9 = Setembro
4 = Abril        |   10 = outubro
5 = Maio         |   11 = Novembro
6 = Junho        |   12 = Dezembro
      """)
#3 saida de dados

match n1:
    case "1":
        resultado = ("Janeiro")
    case "2":
        resultado = ("Fevereiro")
    case "3":
        resultado = ("Março")
    case "4":
        resultado = ("Abril")
    case "5":
        resultado = ("Maio")
    case "6":
        resultado = ("Junho")
    case "7":
        resultado = ("Julho")
    case "8":
        resultado = ("Agosto")
    case "9":
        resultado = ("Setembro")
    case "10":
        resultado = ("Outubro")
    case "11":
        resultado = ("Novembro")
    case "12":
        resultado = ("Dezembro")
    case _:
        resultado = ("Mês invalido")
    
print()
print(f"Resultado: {resultado}")


