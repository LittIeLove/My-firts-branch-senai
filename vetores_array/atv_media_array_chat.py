import os
os.system("clear || cls")

notas = []

def calcular_media(notas):
    for i in range(1, 5):
        nota = float(input(f'Digite a {i}ª nota: '))
        notas.append(nota)
    media = sum(notas) / len(notas)
    return media

def verificar_situacao(media):
    if media >= 7:
        return 'Aprovado'
    elif media >= 5:
        return 'Recuperação'
    else:
        return 'Reprovado'

def mostrar_resultado(notas, media, situacao):
    print('Suas notas foram:')
    for i, nota in enumerate(notas, start=1):
        print(f'Sua {i}ª nota: {nota}')
    print(f'A média do aluno é: {media:.2f}')
    print(f'A situação do aluno é: {situacao}')

# Executando o programa
media_final = calcular_media(notas)
situacao_final = verificar_situacao(media_final)
mostrar_resultado(notas, media_final, situacao_final)