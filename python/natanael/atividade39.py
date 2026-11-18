print("--------------Cadatro de entrega--------------")
for tentativa in range(3):
    entregador = input("Digite o nome do entregador:").strip()
    veiculo = input("Digite o tipo de veículo utilizado para a entrega:").strip()
    cod_pedido = input("Digite o código do pedido:").strip()
    distancia_km = input("Digite a distância da entrega:").strip()
    cidade = input("Digite a cidade de destino da entrega:").strip()
    observação = input("Exite alguma obervação?:").strip()
    
    if entregador.isalpha() >3 and veiculo.isalpha() >3 and cod_pedido >6 and\
        distancia_km.isdigit() and cidade == "Brasília" and\
        observação !="Nenhuma":
            print("Entrega registrada com sucesso.")
            break
    else:
        print("Erro falata.")
else:
    print("Número máximo de tentativas atingido. Tente novamente mais tarde.")
    print("-"*30)