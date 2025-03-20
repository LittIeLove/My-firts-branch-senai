import os
os.system ("clear || cls")

login_cadastrado = "Marta"
senha_cadastrada = "123"
            
for i in range (3):
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    if login_cadastrado == login and senha_cadastrada == senha:
        print("Bem-vindo!")
        break
    else:
        print("Acesso negado.\nTente novamente\n")
        if i == 2:
            print("Número de tentativas acima do permitido.\n")
    
    
      

        

