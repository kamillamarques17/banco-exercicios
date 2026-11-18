senha_cofre = "9988"

for tentativa in range(5):
    senha = input("Digite a senha:").strip()
    if senha == senha_cofre:
          print("Abre!")

else:
     print("ALARME TOCANDO!")