print("---------Acesso ao Wifi-----------")
senha = "cafe2026"
for tentativa in range(3):
    senha_digitada=input("Digite a senha do Wi-fi:")
    if senha_digitada == senha:
        print("Acesso ao Wi-fi liberado!")
        break
    else:
        print("Senha errada, tente novamente.")

else:
    print("Muitas tentativas, tente novamente mais tarde.")    