print("-----------senha segura---------")
for tentativas in range(3):
    senha=input("digite uma senha:").strip()

    if len(senha) >=5:
        print(f"senha '{senha}'aceito!")
        break
    else:
        print(f"nome curto demais: a senha tem que 8 caracteristicas ")
else:
    print("muitas tentativas.")
    print("-"*20)