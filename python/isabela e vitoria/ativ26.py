print("------------------------- CONTA BANCÁRIA --------------------------")

nome = input("Digite o seu nome (mais de 3 caracteres): ").strip()
senha = input("Digite a sua senha (4 caracteres): ").strip()

if len(senha) == 4 and senha != "0000":

    frase = input("Digite a sua frase (mais de 10 caracteres): ").strip()

    if len(nome) > 3 and len(senha) == 4 and len(frase) > 10:
        print(f"Sucesso! Nome: {nome}, Senha: {senha}, Frase: {frase}")
    else:
        print("Acesso negado, verifique seus dados")
