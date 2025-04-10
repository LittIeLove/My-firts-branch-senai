import os
os.system ("clear || cls")

def media(a,b):
    return (a+b) /2

n1 = float(input("Digite sua primeria nota: "))
n2 = float(input("Digite sua segunda nota: "))
mediaf = media(n1,n2)
print(f"A sua media final com as notas ({n1}) e ({n2}) é = ({mediaf})")