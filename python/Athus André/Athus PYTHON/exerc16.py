senha_cafeteria ="cafe2026"
for tentativa in range(3):
    senha = input("Digite a senha do Wi-Fi:").strip()

    if  senha == senha_cafeteria:
     print("Wi-Fi liberado!")
     break
else:
    print("Acesso bloqueado.")