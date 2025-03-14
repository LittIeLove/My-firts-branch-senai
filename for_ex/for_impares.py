import os
import time
os.system ("clear || cls")

#Saida

print("Os números impares ente 1 e 20 são: ")

for i in range(1,21,2):
    print(f"O numero {i} é impar")
    time.sleep(0.2)

#Outra opção

print()
print("Nova tabuada: ")
print()

for u in range (1,21):
    if u % 2 == 1:
        print(f"O número {u} é impar")
print()
print("Fim")