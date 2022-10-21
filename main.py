from cryptography.fernet import Fernet
 
palavra = input("Escreva uma frase")

escolha = input("Digite (f) para escolher a criptografia Fernet ou (c) para escolher a criptografia de césar ")

if escolha == "f":

    key = Fernet.generate_key()
  
    fernet = Fernet(key)
  
    fraseCriptografada = fernet.encrypt(palavra.encode())
  
    fraseDescriptografada = fernet.decrypt(fraseCriptografada).decode()

    print(palavra)
    print(fraseCriptografada)
    print(fraseDescriptografada)

elif escolha == "c":
    print(palavra)
    def criptografar (frase):
        mensagem = ""
    
        for i in palavra:
            mensagem = mensagem + chr (ord(i) + 4)
        return mensagem
    
    print(criptografar(palavra))

    def descriptografar (mensagem):
        frase = ""
    
        for i in palavra:
            frase = frase + chr (ord(i) - 4)
        return frase
    
    
    palavra = criptografar(palavra)   
    print(descriptografar(palavra))

else:
    print("ERRO")
