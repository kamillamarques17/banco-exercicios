senha_celular = "1234"
for tentative in range(4):
    senha = input("Digite a senha do celular: ")


    if senha == senha_celular:
      print("aparelho desbloqueado")
    break
else:
  print("celular fora do ar por 30 minutos")