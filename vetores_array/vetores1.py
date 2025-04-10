import os
os.system ("clear || cls")


notas = []

for i in range (1,4):
    nota = float(input(f"DIgite sua {i}ª nota: "))
    notas.append(nota)

os.system ("clear || cls")
soma = sum(notas)
media = soma / 3

posicao = 0

for nota in notas:
    posicao += 1
    print(f"Sua {posicao}ª nota: {nota} ")
print(f"Media {media:.2f}")




# print(f"Primeira nota:{notas[0]}")
# print(f"Segunda nota:{notas[1]}")
# print(f"Terceira nota:{notas[2]}")
