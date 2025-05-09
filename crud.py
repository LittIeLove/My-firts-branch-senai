#Texto que você quer salvar

texto_para_salvar = "Texto de exemplo que será salvo no arquivo"

#Abre o arquivo (ou cria se não existir) no modo de escrita ("w")

with open ("meu_arquivo.txt", "w") as arquivo:
    #Escreve o texto no arquivo
    arquivo.write (texto_para_salvar)

print("O texto foi salvo com sucesso no arquivo meu_arquivo.txt")
