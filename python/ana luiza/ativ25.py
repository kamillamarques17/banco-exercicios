print("--------------------Cadastro de perfil-------------------")
for tentativa in range(3):
    produto = input ("Digite o produto: ").strip
    código = input ("Digite o código: ").strip
    destino = input ("Digite o destino: ").strip
    if len(produto) and produto !="PROIBIDO" and len(código) == 6 and len(destino) >3:
        print("Produto registrado.")
        break
    else:
        print("Produto não registrado. Tente novamente mais tarde.")
print('-'*45)