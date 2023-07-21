modo = ''
resultado = ''
 
modo = input("Você deseja:\n1 - Criptografar\n2 - Descriptografar\n")
 
if(modo == '1'):
    texto = input("Insira o texto para Criptografar: \n")
 
    for i in range (0, len(texto)):
        resultado = resultado + chr(ord(texto[i]) + 2)
    print(resultado)
    resultado = ''
 
if(modo == '2'):
    texto = input("Insira o texto para descriptografar: \n")
 
    for i in range (0, len(texto)):
        resultado = resultado + chr(ord(texto[i]) - 2)
    print(resultado)
    resultado = ''