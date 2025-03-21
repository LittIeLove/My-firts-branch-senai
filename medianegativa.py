import os
os.system ("clear || cls")
from time import sleep
sequenciaf = 1
nota = 0
nota = float(input("Digite sua primeira nota: "))
if nota < 0:
        print("Apenas números positivos\nRecarregando")
        nota = 0
        sleep(2)

while True:
    sequencia = int(input("Deseja inserir outra nota ? (1) para sim / (qualquer outro numero) para não : "))
    if sequencia == 1:
        sequenciaf += 1
        nota += float(input(f"Digite sua {sequenciaf}ª nota"))
    elif nota < 0:
        print("Apenas números positivos\nRecarregando")
        nota = 0
        sleep(2)
        break

    
