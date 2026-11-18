print("----- TRIAGEM E PRONTUÁRIO MÉDICO -------")

for tentativa in range(5):
    # Coletando e tratando os dados de entrada
    nome = input("Nome do paciente: ").strip()
    especialidade = input("Qual especialidade: ").strip()
    prontuario = input("Número do prontuário: ").strip()
    crm = input("CRM do médico: ").strip()
    convenio = input("Código do convênio: ").strip()
    batimentos = input("Batimentos cardíacos: ").strip()
    temperatura = input("Temperatura corporal: ").strip()
    sala = input("Sala de atendimento: ").strip()
    email = input("Email do hospital: ").strip().lower()
    status = input(
        "Status da triagem (digite URGENTE): "
    ).strip().upper()

    # Validação direta com IF + AND
    if especialidade.isalpha() and \
        nome.isalpha() and \
        prontuario.isdigit() and \
        crm.isalnum() and \
        len(crm) == 7 and \
        convenio.isalnum() and \
        batimentos.isdigit() and \
        temperatura.isdigit() and \
        sala.isdigit() and \
        "@" in email and \
        email.endswith(".med.br") and \
        status == "URGENTE":

        print(
            f"\nSUCESSO: paciente {nome}, "
            f"triagem encaminhada para {especialidade}"
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
        "Procure o atendimento responsável."
    )

