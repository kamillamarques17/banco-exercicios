print("--------------------Cadastro de Perfil de Usuário---------------------")
for tentaiva in range(3):
    Produto = input("Digite o produto:").strip() 
    Código = input("Digite o código:").strip() 
    destino = input("Digite o destino:").strip() 
    if len(Produto) != "proibido" and len(Código) ==6 and len(destino) >3:
        print("Produto registrado")
        break 
    else:
        print("Produto não registrado!")
