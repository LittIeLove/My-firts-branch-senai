import os
os.system ("clear || cls")
from time import sleep
nome = input('Digite seu nome: ')
sequenciaf = 1
nota = float(input("Digite sua primeira nota: "))
notaf = nota
if nota < 0:
    print("Apenas números positivos\nSaindo")
    nota = 0
    sleep(2)
    exit()

while True :
    sequencia = int(input('Você deseja adicionar mais uma nota ? (1) para sim e (qualquer numero) para não: '))
    if sequencia ==1 :
        sequenciaf += 1
        nota = float(input(f"Digite sua a {sequenciaf} nota: "))
        notaf += nota
        if nota < 0:
            os.system ('clear')
            print('Nota negativa\nSequencia encerrada')
            sleep(3)
            break
    else:
        break

media = notaf / sequenciaf


print(f'Nome: {nome}')
print(f'Quantidade de nota: {sequenciaf}')
print(f'Sua media: {media:.2f}')






