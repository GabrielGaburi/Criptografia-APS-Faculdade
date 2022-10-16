from cryptography.fernet import Fernet

with open ("chave.key", "rb") as filekey:
    chave = filekey.read()

Fernet = Fernet(chave)



with open ("arquivo.txt", "rb") as arquivo:
    conteudo_arquivo = arquivo.read()

escolha = input("Escreva criptografar para criptografar o texto ou ou descriptografar para descriptografar o texto")

if escolha == "criptografar":    
    criptografado = Fernet.encrypt(conteudo_arquivo) 

    with open ("arquivo.txt", "wb") as arquivo_criptografado:
        arquivo_criptografado.write(criptografado)

elif escolha == "descriptografar":
    descriptografado = Fernet.decrypt(conteudo_arquivo) 

    with open ("arquivo.txt", "wb") as arquivo_descriptografado:
        arquivo_descriptografado.write(descriptografado)

