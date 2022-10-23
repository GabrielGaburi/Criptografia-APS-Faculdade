from cryptography.fernet import Fernet
 
escolha = input("Digite (f) para escolher a criptografia Fernet ou (c) para escolher a criptografia de césar ")
palavra = input("Escreva uma frase")

if escolha == "f":

    key = Fernet.generate_key() # Criação da chave 
    print(key) # Print da do código da chave
  
    fernet = Fernet(key) # Variável da chave 
  
    fraseCriptografada = fernet.encrypt(palavra.encode()) # Código para a criptografia da frase escolhida
  
    fraseDescriptografada = fernet.decrypt(fraseCriptografada).decode() # Código da descriptografia da frase escolhida

    print("A frase digitada foi......... ",palavra) # Print da frase original escolhida pelo usuário
    print("A frase ficou .......... ", fraseCriptografada) # Print da frase Criptografada
    print("A frase descriptografada ficou........", fraseDescriptografada) # Novamente o print da frase depois de ser descriptografada 

elif escolha == "c":
    print("A frase digitada foi......... ",palavra) # Print da frase original escolhida pelo usuário
    def criptografar (frase): # Função utilizada para a criação da criptografia
        mensagem = ""
    
        for i in palavra:
            mensagem = mensagem + chr (ord(i) + 4) # Parte do código onde converte cada letra da mensagem em um código codificado
        return mensagem
    
    

    def descriptografar (mensagem): # Função utilizada para a criação da descriptografia
        frase = ""
    
        for i in palavra:
            frase = frase + chr (ord(i) - 4) # Parte do código onde descriptografa a frase
        return frase
    
    
    palavra = criptografar(palavra)  
    print("A frase ficou .......... ",criptografar(palavra))  # Print da frase Criptografada  
    print("A frase descriptografada ficou........", descriptografar(palavra)) # Print da frase Descriptografada

else:
    print("ERRO")
