from cryptography.fernet import Fernet
 
escolha = input("Digite (f) para escolher a criptografia Fernet ou (c) para escolher a criptografia de césar ")
palavra = input("Escreva uma frase")

if escolha == "f":

    key = Fernet.generate_key()
  
    fernet = Fernet(key)
  
    fraseCriptografada = fernet.encrypt(palavra.encode())
  
    fraseDescriptografada = fernet.decrypt(fraseCriptografada).decode()

    print("A frase digitada foi......... ",palavra)
    print("A frase ficou .......... ", fraseCriptografada)
    print("A frase descriptografada ficou........", fraseDescriptografada)

elif escolha == "c":
    print("A frase digitada foi......... ",palavra)
    def criptografar (frase):
        mensagem = ""
    
        for i in palavra:
            mensagem = mensagem + chr (ord(i) + 4)
        return mensagem
    
    print("A frase ficou .......... ",criptografar(palavra))

    def descriptografar (mensagem):
        frase = ""
    
        for i in palavra:
            frase = frase + chr (ord(i) - 4)
        return frase
    
    
    palavra = criptografar(palavra)   
    print("A frase descriptografada ficou........", descriptografar(palavra))

else:
    print("ERRO")
