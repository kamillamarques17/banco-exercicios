print("--------------------Conta bancária-------------------")
for tentativa in range(3):
    nome = input ("Digite o nome:")
    senha = input("Digite a senha: ")
    frase = input ("Digite uma frase de segurança: ")
    if len(nome) >3 and len(senha) ==4 and len(frase) >10:
        print("Conta Bancária criada.")
        break
else:
    print("Erro. Tente em outro momento.")
    