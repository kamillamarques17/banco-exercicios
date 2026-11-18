print("-----------------Carga e Destino-----------------")
for tentativa in range(3):
    produto = input("Digite o nome do produto:").strip
    codigo = input("Digite o código do produto:").strip
    destino = input("Digite o seu destino:").strip
    if len(produto) and produto != "PROIBIDO" and len(codigo) == 6 and len(destino)>3:
        print("Entrega registrada!")
