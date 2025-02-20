import os 
os.system ("clear")

idade= int(input("Digite sua idade: "))

if idade <16:
    print("Menores que 16 não podem votar")


elif idade == 16 or idade == 17 :
    print("Voto opicional")

elif idade >= 18 and idade <= 65:
    print("Voto obrigatorio")

else:
    print("Maiores que 65 não são obrigados a votar")
    
    