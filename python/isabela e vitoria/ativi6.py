print("----- CONTROLE DE LOGISTÍCA E DESPACHO DE CARGAS -------")

for tentativa in range(5):
    # Coletando e tratando os dados de entrada
    nome_motorista = input("Nome do motorista: ").strip()
    cidade_destino = input("Nome da cidade de destino: ").strip()
    placa = input("placa: ").strip()
    codigo = input("codigo: ").strip()
    peso= input("peso: ").strip()
    nota_fiscal = input("número da nota fiscall: ").strip()
    transporte = input("tipo de transporte: ").strip()
    email = input("email: ").strip()
    CEP = input("cep: ").strip()
    status = input("Confirmar status (digite AUTORIZADO): ").strip().upper()

    # Validação direta com IF + AND
    if nome_motorista.isalpha() and \
       cidade_destino.isalpha() and \
       transporte.isalpha() and \
       placa.isalnum() and \
       codigo.isalnum() and \
       peso.isdigit and \
       nota_fiscal.isdigit and \
       CEP.isdigit and \
       len(CEP) == 8 and \
       email.endswith("log.br") and \
        status == "AUTORIZADO":

       print(
            f"\nSUCESSO: cliente {nome_motorista}, "
            f"tudo certo"
        )
       break
    else:
        # Exibe a tentativa amigável (1 a 5)
        print(f"\nERRO: dados inválidos, tentativa {tentativa + 1} de 5")
        print("-" * 40)

else:
 print(
        "\nBLOQUEADO: limite de 5 tentativas excedido. "
        "Procure o suporte da corretora."
    )
