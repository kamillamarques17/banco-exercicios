tipo_motorista = input("Qual a cor do semáforo? (1: Vermelho / 2: Amarelo / 3: Verde): ")
if tipo_motorista == "1":
    print("Pare o carro!")
elif tipo_motorista == "2":
    print("Atenção...")
elif tipo_motorista == "3":
    print("Siga em frente!")
else:
    print("Opção inválida.")