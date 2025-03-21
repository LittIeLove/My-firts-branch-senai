import os
os.system ("clear || cls")

nome = input("Digite seu nome: ")
nota = float(input("Digite sua a nota: "))

sequencia = 1
mediaf = 1
while True:
    repetir = int(input("Deseja adicionar mais uma nota ? Para sim (1) / para não (qualquer caracter): "))
    if repetir == 1:
        os.system ("clear || cls")
        sequencia += 1
        nota += float(input(f"Digite a {sequencia}ª Nota: "))
        mediaf += 1
    else:
        os.system ("clear || cls")
        break

print(f"Nome:{nome}")
print(f"Quantidade de notas inceridas {mediaf}")
print(f"A media final é: ({nota / mediaf})")



