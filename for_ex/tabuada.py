import os
import time
os.system ("clear || cls")

#Entrada de dados

n1 = int(input("Qual tabuada você deseja ver ? : "))

os.system ("clear || cls")

print("A tabuada é :\n ")

#Saida de dados

for i in range(1,11):
    multi= n1 * i
    print(f" {n1} x {i} = {multi}\n ")
    time.sleep(0.3)

print("Fim da execucão")
exit()
