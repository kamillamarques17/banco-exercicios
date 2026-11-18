print("----- TERMINAL DE AUTOATENDIMENTO -------")

for tentativa in range(5):
    # Coletando e tratando os dados de entrada
    nome = input("Nome do Correntista: ").strip()
    conta = input("Tipo de conta: ").strip()
    agencia = input("Número da agência: ").strip()
    cartao = input("Número do cartão: ").strip()
    valor = input("Valor do saque: ").strip()
    pin = input("PIN de segurança: ").strip()
    codigo = input("Código do terminal: ").strip()
    cidade = input("Cidade do caixa: ").strip()
    email = input("Email de notificação: ").strip().lower()
    status = input(
        "Status da operação (digite CONCLUIDO): "
    ).strip().upper()

    # Validação direta com IF + AND
    if nome.isalpha() and \
        conta.isalpha() and \
        agencia.isdigit() and \
        cartao.isdigit() and \
        valor.isdigit() and \
        pin.isdigit() and \
        len(pin) == 4 and \
        codigo.isalnum() and \
        cidade.isalpha() and \
        "@" in email and \
        email.endswith(".bank.com") and \
        status == "CONCLUIDO":

        print(
            f"\nSUCESSO: correntista {nome}, "
            f"saque realizado com sucesso!"
        )
        break

    else:
        print(
            f"\nERRO: dados inválidos, tentativa "
            f"{tentativa + 1} de 5"
        )
        print("-" * 40)

else:
    print(
        "\nBLOQUEADO: limite de 5 tentativas excedido. "
        "Procure o suporte."
    )
