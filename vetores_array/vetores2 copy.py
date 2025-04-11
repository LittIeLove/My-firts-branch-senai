import os
os.system ("clear || cls")
from time import sleep

notas = []

def media(notas):
    try:

        for i in range (1,5):
            nota = float(input(f"Digite sua {i}ª nota: "))
            notas.append(nota)
    except ValueError:
        print("Apenas números\nRecomeçe.")
        sleep(1)
        exit()

    media = sum(notas) / len(notas)
    return media
       


def situacao(media):
    if media >= 7:
        return  'Aprovado'
    elif media >= 5:
        return  'Recuperação'
    else:
        return  'Reprovado'    
    
os.system ("clear || cls")

def mostrar_resultados(notas, media, situacao):
    print("Suas notas foram.")
    for i, nota in enumerate(notas, start = 1):  #enumerate é uma função que transforma a lista em algo que te dá o índice (posição) e o valor ao mesmo tempo enquanto percorre a lista.
        print(f'A sua {i}ª nota é : {nota}')
    print(f"Sua media é : {media:.2f}\nSituação: {situacao}")

media_final = media(notas)
situacao_final = situacao(media_final) #Está chamando a função verificar_situacao(), passando a média que acabou de calcular. serve para enviar a media para o segundo def que usará no if
mostrar_resultados (notas, media_final , situacao_final) #Não usar = 




      


        