import os
import time
os.system ("clear || cls")

n1 = int(input("Digite o começo da contagem até 1: "))
timer = float(input("Digite o timer desejado: "))
for i in range(n1, 0,-1):
    print(i)
    time.sleep(timer)

print("Fim")

