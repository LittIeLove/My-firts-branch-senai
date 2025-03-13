import os
import time
os.system ("clear || cls")

print("De 100 ate 120 em par")

for i in range(100,121,2):
    print(f"Numeros: {i}")
    time.sleep(0.3)



os.system ("clear || cls")


print("Pares 100 até 120: ")
for i in range(100,121):
    if i % 2 ==0:
        print(f"Numeros: {i}")
        time.sleep(0.3)

print("Acabou")