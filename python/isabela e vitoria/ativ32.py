print("------ AGENDAMENTO DE OFICINA ------")

for tentativa in range(2):
    cliente = input("Digite o cliente: ").strip()
    veiculo = input("Digite o veículo: ").strip()
    placa = input("Digite a placa (7 caracteres): ").strip()
    km = input("Digite o KM: ").strip()
    servico = input("Digite o serviço: ").strip()
    codigo = input("Digite o código técnico: ").strip()

    if len(cliente) > 3 and len(veiculo) > 3 and \
       len(placa) == 7 and \
       km.isdigit() and \
       servico != "TESTE" and \
       codigo == "T100":
        
        print("Agendamento realizado com sucesso!")
        break
    else:
        print("Erro: Verifique os dados digitados.")  
        print("-" * 30)