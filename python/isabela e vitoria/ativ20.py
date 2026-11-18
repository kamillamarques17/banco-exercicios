print("-------------------------LOGIN COM NOME DE USUARIO--------------------------")
for tentativas in range(3) :
 senha = input("Digite seu nome de usuario: ").strip()

 if len(senha) >= 5:
   print(f"acesso liberado, {senha}")
   break
 else:
  print("nome muito curto,tente novamente")
else:
  print("acabaram as tenativas")