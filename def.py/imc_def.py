import os
os.system ("cls || clear")



def imc ():
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc_final = peso / (altura * altura)
    return imc_final

imc_paramatch = imc() 
os.system ("clear || cls")   

if imc_paramatch < 18.5:
    print(f"Abaixo do peso {imc_paramatch:.2f}\nConsulte um nutricionista para orientação.")

elif imc_paramatch < 25:
    print(f"Peso normal {imc_paramatch:.2f}\n Mantenha Hábitos saudáveis\nConsidere uma dieta balanceada e atividade física")

elif imc_paramatch < 30 :
    print(f"Sobrepeso {imc_paramatch:.2f}\nConsidere uma dieta balanceada e atividade física.")

elif imc_paramatch < 35:
    print(f"Obesidade grau 1 {imc_paramatch:.2f}\n procure uma orientação de um profissional de saúde.")

elif imc_paramatch < 40:
    print(f"Obesidade grau 2 {imc_paramatch:.2f}\Cosulte um médico para avaliação e orientção.")

else:
    print(f"Obesidade grau 3 {imc_paramatch:.2f}\nBusque assitência mêdica imediatamente.")