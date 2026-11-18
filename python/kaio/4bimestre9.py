print("----------------Sistema Municipal de Trânsito e Notificação de Infrações---------------------")

for tentativas in range(5):
    nome_condutor = input("Nome do condutor: ").strip()
    sobrenome = input("Digite o sobrenome do condutor: ").strip()
    bairro_infração = input("Digite o Bairro da infração: ").strip()
    município_registro = input("Digite o municio de registro: ").strip()
    placa_veiculo = input("Digite a placa do veiculo: ").strip().upper()
    código_infração = input("Digite o Codigo de infração: ").strip()
    velocidade_aferida= input("Digite a velocidade aferida: ").strip()
    limite_via= input("Digite o limite da via: ").strip()
    data = input("Data da Expedição (DD/MM/AAAA): ").strip()
    email = input("E-mail do Detran: ").strip()
    codigo = input("Digite o codigo do radar (MULTA): ").strip().upper()
    validação = input("Status (EMITIDO): ").strip()

    if nome_condutor.isalpha() and \
            sobrenome.isalpha() and \
            bairro_infração.isalpha() and \
            município_registro.isalpha() and \
            placa_veiculo.startswith("DATA-") and placa_veiculo[4:].isalnum() and \
            código_infração.isalnum() and \
            velocidade_aferida.isdigit() and \
            limite_via.isdigit() and \
            len(data) == 10 and data.count("/") == 2 and \
            email.count("@") and email.endswith(".detran.gov.br") and \
            codigo == "MULTA" and \
            validação == "ABERTO":
        
        print(f"\nSUCESSO: titular {nome_condutor}, Condutor autorizado!")
        break

    else:
        print(f"\nERRO: Dados invalidos! {tentativas + 1} de 5")
        print("-" * 40)

else:
    print("\nAcesso negado")