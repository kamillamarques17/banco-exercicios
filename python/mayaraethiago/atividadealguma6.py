print("--- Sistema de Controle de Logística e Despacho de Cargas ---")

for tentativa in range(5):
    motorista = input("Nome do Motorista: ").strip()
    cidade = input("Cidade de Destino: ").strip()
    placa = input("Placa do Veículo: ").strip().upper()
    rastreamento = input("Código de Rastreamento: ").strip().upper()
    peso = input("Peso da Carga (kg): ").strip()
    nota = input("Número da Nota Fiscal: ").strip()
    transporte = input("Tipo de Transporte: ").strip()
    email = input("E-mail da Transportadora: ").strip().lower()
    cep = input("CEP da Entrega: ").strip()
    status = input("Status do Envio (Digite AUTORIZADO): ").strip().upper()

    if motorista.isalpha() and \
       cidade.isalpha() and \
       placa.isalnum() and \
       rastreamento.isalnum() and \
       peso.isdigit() and \
       nota.isdigit() and \
       len(cep) == 8 and \
       "@" in email and \
       email.endswith("log.br") and \
       status == "AUTORIZADO":

        print(f"\nSucesso: Carga liberada para o motorista {motorista}!")
        break

    else:

        print(f"\nERRO: Dados inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)

else:

    print("\nBLOQUEADO: Limite de 5 tentativas excedido.")
