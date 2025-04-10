def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

def potencia(x, y):
    return x ** y

def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potência")
        print("6. Sair")

        operacao = input("Digite o número da operação (1/2/3/4/5/6): ")

        if operacao == '6':
            print("Saindo da calculadora... Até logo!")
            break

        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Por favor, digite números válidos.")
            continue

        if operacao == '1':
            print(f"{numero1} + {numero2} = {soma(numero1, numero2)}")

        elif operacao == '2':
            print(f"{numero1} - {numero2} = {subtracao(numero1, numero2)}")

        elif operacao == '3':
            print(f"{numero1} * {numero2} = {multiplicacao(numero1, numero2)}")

        elif operacao == '4':
            print(f"{numero1} / {numero2} = {divisao(numero1, numero2)}")

        elif operacao == '5':
            print(f"{numero1} ^ {numero2} = {potencia(numero1, numero2)}")

        else:
            print("Operação inválida! Por favor, escolha uma operação válida.")

# Chama a função da calculadora
calculadora()
