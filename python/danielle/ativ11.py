senha_correta = "Naotemsenha1*"
for tentaiva in range(3): 
    senha = input("olá, digite a senha:")
    if senha == senha_correta: 
     print("Acesso Permitido")
     break
    else:
       print("Senha incorreta!")
else:
   print("Conta bloqueada")