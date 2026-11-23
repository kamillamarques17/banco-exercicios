email_salvo = "nakimaerr@gmail.com"
senha_salva = "12345"

for tentativa in range(3):
    email_digitado = input("Digite o seu e-mail: ")
    senha_digitada = input("Digite a sua senha: ")

    if email_digitado == email_salvo and senha_digitada == senha_salva:
        print("Login efetuado com sucesso!")
        break
    else:
              print(f"Dados incorretos!")
else:
      print("Acesso bloqueado. Contacte o suporte.")