senha_correta="996606"
for tentativas in range(3):
    chute = input("digite uma senha")
    if chute == senha_correta:
        print("acesso permitido")
        break
    else:
        print("senha incorreta.")
    