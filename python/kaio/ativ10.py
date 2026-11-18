senha_correta = "12345"
email_correto = "admin@email.com"

for tentativa in range(3):

    email = input("Email de acesso: ")
    senha = input("Digite a sua senha: ")
    if email == email_correto and senha == senha_correta:
        print("Senha correta! Entrando... ")
        break
    else:
        print("Senha icorreta")
else:
    
       print("Conta bloqueada após 3 tentativas falhas.")