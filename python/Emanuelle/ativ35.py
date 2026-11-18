print("----------------Reserva de veículo de luxo----------------")
for tentativa in range(3):
    cliente = input("cliente: ").strip()
    veículo = input("veículo: ").strip()
    cor = input("cor do carro: ").strip()
    CNH = input("CNH (9 números): ").strip()
    dias = input("Digite os dias do aluguel: ").strip()
    seguro = input("seguro: ").strip()

    if cliente.isalpha() > 3  and veículo =="SEDAN"  and \
       cor > 3 and CNH.isdigit() and \
       len(dias) > 3  and seguro > 3 and \
       print("Reservado!"):
       break 
    else: 
       print("Erro ao reservar.")
       print("-" * 30)
else:
  print("Erro na reserva.")
