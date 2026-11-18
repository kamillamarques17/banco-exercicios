senha_correta = "1234"
for tentativas in range(4) :
    chute = input("Digite a senha wifi-fi: ")
    if chute == senha_correta:
        print("Celular desbloqueado")
        break
    else:
         print("Celular inoperante por 30 minutos")