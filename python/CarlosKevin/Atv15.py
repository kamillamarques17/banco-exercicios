for i in range(10):
    quantidade = int(input("Quantas camisetas o cliente quer comprar? "))
    
    if quantidade <= 5:
        print("Venda realizada")
    else:
        print("Quantidade indisponível no estoque")