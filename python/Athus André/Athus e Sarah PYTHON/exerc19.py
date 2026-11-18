usuarios_corretos = ["Administrador", "Root", "Suporte"]
for usuarios_corretos in range(3):
 tentativa = input("Selecione o usuário: ")
 if tentativa == usuarios_corretos:
    print("Usuário proibido, tente novamente.")
    break
 else:
  print("Usuário desbloqueado com sucesso.")