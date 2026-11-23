senha_correta = "12345"
email_correto = "admin@email.com"
for tentativa in range(3):
    chute_mail = input("Digite seu email: ")
    chute_senha = input("Digite sua senha: ")
    if chute_mail == email_correto and chute_senha == senha_correta:
        print("Login efetuado")
        break
    else:
        print("Dado incorretos, tente novamente")
else:
    print("conta bloqueada após 3 tentativas falhas. ")