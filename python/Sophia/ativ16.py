senha_cafeteria ="cafe2026"
for tentativa in range(3):
    senha = input("Digite a senha do wi-fi:")


    if  senha == senha_cafeteria:
     print("Wi-fi liberado")
     break
else:
    print("Acesso bloqueado")
