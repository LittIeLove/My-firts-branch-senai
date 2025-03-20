import os
os.system ("clear || cls") #LIMPANDO DADOS


#VARIAVEIS PARA SOMAR OS DADOS

par = 0
impar = 0

#ENTRADA DE DADOS

for i in range (5):
    ns = int(input("Digite um número: "))
    if ns %2 == 0:
        par += 1
    else:
        impar += 1

os.system ("clear || cls") #LIMPANDO DADOS


print(f"Entre os numeros são {par} par e {impar} impar")

