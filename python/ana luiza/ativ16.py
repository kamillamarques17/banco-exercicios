senha_correta = "café2026"

for tentativa in range(3):
 tentativa=input("Digite a senha:")
 if tentativa == senha_correta:
   print("Acesso Permitido")
   break
else:
  print("Acesso negado")

