print("----- SISTEMA DE ACESSO SEGURO -------")

for tentativa in range(5):
    # Coletando e tratando os dados de entrada
    nome_adm = input("Nome do administrador: ").strip()
    cargo_usuario = input("Nome do cargo: ").strip()
    cod_servidor = input("Código do servidor: ").strip()
    ip_terminal = input("IP terminal: ").strip()
    porta_rede = input("Porta de rede: ").strip()
    setor_responsavel = input("Setor responsável: ").strip().lower()
    protocolo_rede = input("Protocolo de rede: ").strip()
    senha_provisoria = input("Senha provisória: ").strip()
    dominio_corporativo = input("Domínio corporativo: ").strip()
    autenticacao = input(
        "Confirmar autenticação (digite LIBERADO): "
    ).strip().upper()

    # Validação direta com IF + AND
    if porta_rede.isdigit() and \
        ip_terminal.isdigit() and \
        protocolo_rede.isalnum() and \
        cod_servidor.isalnum() and \
        cargo_usuario.isalpha() and \
        setor_responsavel.isalpha() and \
        dominio_corporativo.endswith(".org") and \
        len(senha_provisoria) > 8 and \
        autenticacao == "LIBERADO":

        print(
            f"\nSUCESSO: administrador {nome_adm} "
            f"autenticado com sucesso!"
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

