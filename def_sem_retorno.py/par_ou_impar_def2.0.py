import os
os.system ("clear || cls")
while True:
    def numeros(par_impar):
        par = 0
        impar = 0
        os.system ("clear || cls")
        if par_impar == 0:
            exit()
        elif par_impar % 2 == 0:
            print(f"O numero {par_impar} é par")

        elif par_impar % 2 == 1:
            print(f"O numero {par_impar} é impar")

        
        else:
            print("Digito invalido")
    nu1 = int(input("Digite um número (Digite o numero (0) para encerrar): "))
    print
    numeros(nu1)
