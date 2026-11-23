print("--------------------Criação de Conta Bancária Completa---------------------")
for tentaiva in range(3):
    Nome = input("Digite o Nome:").strip() 
    Senha = input("Digite a senha:").strip() 
    Frase = input("Digite uma frase de segurança:").strip()
    if len(Nome) >3 and len(Senha) ==4 and len(Frase) >10:
     print("Conta bancária criada")
    break 
else:
    print("recusada!")
