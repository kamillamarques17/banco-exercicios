senha_correta = "python"

for tentativa in range(4):
    senha = input("Digite a senha:")
    if senha == senha_correta:
     print("Login realizado")
     break
    else:
       print("Senha incorreta")
else:
   print("Acesso bloqueado")