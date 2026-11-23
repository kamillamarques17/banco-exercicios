print("----- SISTEMA DE REGISTRO DE CRIPTOATIVO -------")

for tentativa in range(5):
    # Coletando e tratando os dados de entrada
    nome_cliente = input("Nome do cliente: ").strip()
    nome_criptomoeda = input("Nome da criptomoeda: ").strip()
    cod_hash = input("Código hash da carteira: ").strip()
    data = input("Data da transação: ").strip()
    id_bloco = input("ID numérico do bloco: ").strip()
    email_suporte = input("Email de suporte: ").strip().lower()
    quantidade = input("Quantidade de moedas: ").strip()
    cod_taxa = input("Código de taxa: ").strip()
    pais_corretora = input("País da corretora: ").strip()
    autenticacao = input("Confirmar autenticação (digite APROVADO): ").strip().upper()

    # Validação direta com IF + AND
    if nome_criptomoeda.isalnum() and \
        cod_hash.isalnum() and \
        id_bloco.isdigit() and \
        quantidade.isdigit() and \
        pais_corretora.isalpha() and \
        "@" in email_suporte and \
        email_suporte.endswith("crypto.com") and \
        len(data) == 10 and \
        autenticacao == "APROVADO":

        print(
            f"\nSUCESSO: cliente {nome_cliente}, "
            f"criptomoeda {nome_criptomoeda} registrada"
        )
        break
    else:
        print(f"\nERRO: dados inválidos, tentativa {tentativa + 1} de 5")
        print("-" * 40)
else:
    print(
        "\nBLOQUEADO: limite de 5 tentativas excedido. "
        "Procure o suporte da corretora."
    )
