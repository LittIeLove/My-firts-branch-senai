import os
os.system ("clear || cls")
import time

print("Contagem regressiva. ")

for i in range(10,-2,-1):
    print(f"Valor da variável i : {i}")
    time.sleep(0.1)
    print("Acabou")
