senha_correta = "1234"

for tentativa in range(4):
 tentativa=input("Digite a senha:")
 if tentativa == senha_correta:
   print("Aparelho Desbloqueado")
   break
else:
  print("Celular Inoperante por 30 minutos")
