email_salvo = "thebest@gmail.com"
senha_salvo = "12345"

for tentativa in range(3):
    email_digitado = input("Digite o seu email: ")
    senha_digitada = input("Digite sua senha")
    
    if email_digitado == email_salvo and senha_digitada == senha_salvo:
        print("Login efetuado com sucesso!")
        break
    else:
        print(f"Dados incorretos")
        
else:
    print("Acesso bloqueado. Contacte o suporte.")