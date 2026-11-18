print("----- SISTEMA DE LANÇAMENTO ESPACIAL -------")

for tentativa in range(5):
    # Coletando e tratando os dados de entrada
    missao = input("Nome da missão: ").strip()
    cod_foguete = input("Código do foguete (ex: APOLLO11): ").strip().upper()
    data = input("Data do lançamento: ").strip()
    id_astronauta = input("ID digital do astronauta: ").strip()
    email_base = input("Email da base: ").strip().lower()
    combustivel = input("Nível de combustível (apenas números): ").strip()
    carga = input("Carga espacial: ").strip()
    pressao = input("Pressão da cabine: ").strip()
    cidade = input("Cidade de origem: ").strip()
    status = input("Status (digite APROVADO): ").strip().upper()

    # Validação direta com IF + AND
    if cod_foguete.isalnum() and \
        carga.isalnum() and \
        id_astronauta.isdigit() and \
        combustivel.isdigit() and \
        pressao.isdigit() and \
        cidade.isalpha() and \
        email_base.endswith(".gov.br") and \
        len(data) == 10 and \
        status == "APROVADO":

        print(
            f"\nSUCESSO: astronauta {id_astronauta}, "
            f"foguete {cod_foguete} liberado"
        )
        break

    else:
        # Exibe a tentativa amigável (1 a 5)
        print(f"\nERRO: dados inválidos, tentativa {tentativa + 1} de 5")
        print("-" * 40)

else:
    print(
        "\nBLOQUEADO: limite de 5 tentativas excedido. "
        "Procure o diretor da base."
    )
