print("------------login de usuario---------")
for tentativas in range(3):
    usuario=input("digite seu nome de usuario:").strip()

    if len(usuario) >=5:
        print(f"usuario '{usuario}'aceito!")
        break
    else:
        print(f"nome curto demais:")
else:
    print("muitas tentativas.")
    print("-"*20)