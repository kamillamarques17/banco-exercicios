for tentativa in range(3):
 senha = input("Digite sua senha: ").strip()

 if len(senha) >= 8:
  print(f"Senha correta! {senha}")
  break
 else:
  print("Senha invalidade: ela deve ter exatamente 8 caracteres.")
else:
 print("Acabaram as tentativas")