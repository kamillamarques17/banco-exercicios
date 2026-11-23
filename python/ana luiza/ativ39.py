print("----------Cadastro de entrega----------")
for tentativa in range(3):
    entregador = input("Nome do entregador: ").strip()
    veiculo = input("Qual o seu veiculo?: ").strip()
    cod_pedido = input("Qual o codigo do pedido?: ").strip()
    distancia_km = input("Qual a distancia?: ").strip()
    cidade = input("Digite a sua cidade: ").strip()
    observação = input("Tem alguma observação?: ").strip()

    if entregador.isalpha() and veiculo.isalpha() > 3 and cod_pedido > 6 and distancia_km.isdigit and cidade == "Brasilia" and observação != "Nenhuma": 
        print("Cadastro concluido")
        break
    else:
        print("Erro fatal.")
else:
    print("Tentativas bloqueadas.")
    print("-"*30)
