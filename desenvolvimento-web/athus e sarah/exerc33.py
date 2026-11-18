print('-----Sistema de Agendamento de Oficina-----')
for tentativa in range(3):
    cliente = input("Nome: ").strip()
    veiculo = input("Nome do veículo: ").strip()
    placa = input("Nº Placa (7 dígitos): ").strip()
    km = input("KMs andados: ").strip()
    serviço = input("Que serviço deseja fazer? ").strip()
    cod_tec = input("Digite o código técnico: ").strip()

    if len(cliente) > 3 and len(veiculo) > 3 and \
       len(placa) == 7 and km.isdigit() and \
       serviço != "TESTE" and cod_tec == "T100":
        
         print("Pedido agendado com sucesso!")
         break
    else:
        print("Erro: Verifique os dados.")
else:
    print("Muitas tentativas. Procure a secretaria.")
print('-'*42)