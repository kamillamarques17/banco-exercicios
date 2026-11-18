email_correta = "admin@emali"
senha_correta = "12345"
for tentativa in range(3):
 chute_mail = input("Digite o seu email: ")
 chute_senha = input("Digite a sua senha: ")
 if chute_mail == email_correta and chute_senha == senha_correta:
    print("login efetuado")
    break
 else:
  print("Dados incoretos, tente novamente")
else:
 print("conta bloqueada após 3 tentativas falhadas")