import os   
os.system ("clear || cls")

while True:
    nota = float(input("Digite a sua nota: "))

    if nota < 0 or nota > 10:
        print("Nota invalida")
        nota = float(input("Digite a sua nota: "))

    else:
        break


print (nota)
                 
    