print("-----------Sistema de duas etapas-----------")
codigo_salvo = "123"
senha_salvo = "messithebest"
for tentativa in range(3):
    codigo = input("Digite o código de área:")
    senha = input("Digite a senha: ")
    if codigo == codigo_salvo and senha == senha_salvo:
        print("Acesso concedido!")
        break
else:
    print("Acesso negado!")
    