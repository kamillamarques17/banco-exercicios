senha_blublu = "blublu"
for tentativa in range(1):
    aposta = input("Digite a senha: ")
    if aposta == senha_blublu:
        print("Acesso Permitido.")
        break
else:
    print("Senha incorreta.")