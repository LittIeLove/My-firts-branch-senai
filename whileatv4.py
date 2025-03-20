import os
os.system ("clear || cls ")

soma = 0

for i in range(3):
    while True:
        nota = float(input(f"Digite a {i + 1}ª nota: "))
        if nota < 0 or nota > 10:
            print("Nota invalida, tente novamente.")
        
        else:
            soma += nota
            break

final = soma / 3     
if final > 7:
   situação = "aprovado"
elif final >=5:
    situação = "recuperação"
else:
    situação = "reprovado"

print(f"Sua media é ({final})")
print(f"Situação {situação}")

