print('----- Sistema de Agendamentp de Oficina-----')
for tentativa in range (3):
    cliente = input ("Nome do cliente (3 caracteres):").strip()
    veiculo =input ("Nome do veiculo (3 caracteres):").strip()
    placa = input ("Digite a placa do carro (7 caracteres):").strip()
    km = input ("Quantos km o carro rodou:").strip()
    serviços = input (" Qual serviço deseja:").strip()
    código = input ("Digite o código:").strip()

    if len(cliente) > 3 and len(veiculo) > 3 and \
        len(placa) == 7 and km.isdigit() and \
        serviços != "TESTE" and código == "T100":

        print ("Pedido agendado com Sucesso!")
        break
    else:
        print("Pedido agendado com sucesso!")
else:
    print("Muitas tentativas. Procure a secretaria.")
print('-'*42)