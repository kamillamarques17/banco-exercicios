print("------------------SENHA SEGURA COM CONFIRMAÇÃO E TAMANHO------------------------")

for tentativa in range(3):
    senha = input("Dedina sua senha(8 caracteres): ").strip()
    if len(senha) < 8:
      print("Senha inválida: ela deve ter exatamente 8 caracteres!")
      break
    else: 
     print("Senha definida com sucesso.")
     print("-"*50)
else: 
  print("LImite de tentativa atingidas.")

