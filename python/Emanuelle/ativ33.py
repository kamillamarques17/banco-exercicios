print("---------Sistemade Agendamento de Oficina-------------")
for tentativa in range(3):
    cliente = input("Cliente: ").strip()
    veículo = input("Veículo: ").strip()
    placa = input("Placa (7 números): ").strip()
    KM = input("KMs andados: ").strip()
    serviço = input(" Que serviço deseja fazer? ").strip()
    codigo = input("Código técnico: ").strip()
 

    if len(cliente) > 3 and  len(veículo) > 3 and \
       len(placa) == 7 and KM.isdigit() and \
       serviço != "TESTE" and codigo == "T100":
       
       
        print("Pedido agendado.")
        break 
    else: 
        print("Erro: Verifique os dados.")
        print("-" * 30)
else:
    print("Muitas tentativas falhas.")
