senha_correta = "cafe2026"
for tentativas in range(3) :
    chute = input("Digite a senha wifi-fi: ")
    if chute == senha_correta:
        print("Wi-fi liberado")
        break
    else:
         print("Acesso bloqueado")