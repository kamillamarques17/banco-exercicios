print("----------O SISTEMA DE SEGURANÇA EM DUAS ETAPAS----------")
nome = input("Olá! digite seu nome: ")
senha = input("Agora, digite sua senha: ")
frase_seguranca = input("Por último, digite a frase de segurança: ")
for tentativa in range(3):
    if len(nome) > 3  and len(senha) == 4 and len(senha) != "0000" and len(frase_seguranca) > 10:
         print("Registrado com sucesso!")
         break
else:
     print("Falha em registrar.")
print('-'*50)