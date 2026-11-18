senha_correta="996606"
email_extra = "daniel@email.com"
for tentativas in range(3):
    chute = input("digite a senha (ou e-mail de acesso):")
    if chute == senha_correta or chute == email_extra:
        print("acesso liberado")
        break
    else:
        print("incorreto.")
else:
    print("conta bloqueada.")
    

