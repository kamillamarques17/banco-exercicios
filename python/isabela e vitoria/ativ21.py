print("-------------------------SEGURANÇA COM CONFIRMAÇÃO E TAMANHO--------------------------")
for tentativas in range(3) :
 senha = input("Digite sua senha: ").strip()

 if len(senha) == 8:
   print(f"senha definida com sucesso, {senha}")
   break
 else:
  print("senha invalida")
