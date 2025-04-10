import os
os.system ("clear || cls")


notas = []

for i in range(1,5):
    nota = float(input(f"Digite sua {i}ª nota: "))
    notas.append(nota)

def media (notas):
    soma = sum(notas)
    mediaf = soma / 4
    return mediaf
media_final = media(notas)

def resultado (media_final):
    if media_final >= 7:
        return f"Aprovado\nNotas: {notas}\nMedia: {media_final}"
    
    elif media_final >= 5:
        return f"Recuperação\nNotas: {notas}\nMedia: {media_final}"

    else:
        return f"Reprovado\nNotas: {notas}\nMedia: {media_final}"

resultado(media_final)




    
        