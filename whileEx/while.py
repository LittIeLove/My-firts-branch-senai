import os 
os.system ("clear || cls")


#Exemplo de uso de laço de repetição while.
idade = int(input("Digite sua idade: "))

while idade < 18:
    print("Não autorizado. \nSomente maiores de 18.\n")
    idade= int(input("Digite sua idade: "))

os.system ("clear || cls ")
print("Acesso permitido")
print("Fim.")