print("-------------LOGIN COM NOME DE USUÁRIO-----------------")

for tentativa in range(3):
    nome = input("Digite o nome do usuário (5 caracteres): ").strip()

    if len(nome) < 5:
        print(f"Nome {nome} muito curto!")
        break
    else: 
        print(f"Usuário {nome} aceito!")
        print("-"*40)
else: 
    print("Limite de tentaivas atingidas. ")