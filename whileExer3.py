import os   
os.system ("clear || cls")


while True:
     n1 = float(input("Digite sua primeira nota: "))
     n2 = float(input("Digite sua segunda nota: "))
     if n1 < 0 or n1 > 10 and n2 < 0 or n2 > 10:
          print("Notas invalidas (Maximo de 0 até 10)")
     elif n1 < 0 or n1 > 10:
          print("Primeira nota invalida (Maximo de 0 até 10)")
     elif n2 < 0 or n2 > 10:
          print("Segunda nota invalida (Maximo de 0 até 10)")
     else:
          break

print(f"Sua media é {(n1 + n2) / 2}")