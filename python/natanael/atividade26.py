print("------------------------Criação de Conta Bancária completa-----------------------------")
for tentativa in range(3):
    nome = input('Digite o nome:').strip()
    senha = input("Digite a senha:").strip()
    frase = input("Digite uma frase de segurança:").strip()
    if len(nome) >3 and len(senha) ==4 and len(frase) >10:
        print("conta bancária criada")
        break
else:
    print("Recusada!")