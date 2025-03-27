numeros_lidos = 0
numeros_pares = 0
numeros_impares = 0
soma_pares = 0
soma_geral = 0

while True:
    numero = int(input('Digite um numero inteiro positivo (0 para sair): '))

    if numero == 0:
        break
    if numero % 2 == 0:
        numeros_pares += 1
        soma_pares += numero
    else:
        numeros_impares += 1

soma_geral += numero
numeros_lidos += 1


media_pares = soma_pares / numeros_pares if numeros_pares > 0 else 0
media_geral = soma_geral / numeros_lidos if numeros_lidos > 0 else 0


print(f'Quantidade de numeros pares {numeros_pares}')
print(f'Quantidade de numeros impares {numeros_impares}')
print(f'Media dos valores pares: {media_pares:.2f}')
print(f'media geral dos numeros lidos {media_geral:.2f}')