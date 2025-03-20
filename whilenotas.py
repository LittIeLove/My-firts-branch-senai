import os   
os.system ("clear || cls")
QUANTIDADE_NOTAS = 2
soma = 0


for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            os.system ("clear || cls")
            print("Nota invalida, tente novamente\n")

        else:
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS

print(f"Média {media}")