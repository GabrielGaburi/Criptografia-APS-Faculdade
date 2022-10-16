
palavra = input("Digite qualquer coisa")
def criptografar (frase):
    mensagem = ""
    
    for i in palavra:
        mensagem = mensagem + chr (ord(i) + 1)
    return mensagem
    
print(criptografar(palavra))

def descriptografar (mensagem):
    frase = ""
    
    for i in palavra:
        frase = frase + chr (ord(i) - 1)
    return frase
     
palavra = criptografar(palavra)   
print(descriptografar(palavra))
    

