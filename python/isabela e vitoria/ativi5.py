print("----- CADASTRO DE DESENVOLVEDORES E REPOSITORIO GIFT -------")

for tentativa in range(5):
    # Coletando e tratando os dados de entrada
    nome_desenvolvedor = input("Nome do desenvolvedor: ").strip()
    nickname_git = input("Nome da nickname: ").strip()
    nome_repositorio = input("nome repositorio: ").strip()
    id_commit = input("id commit: ").strip()
    quant_linhas= input("Iquantidade de linhas: ").strip()
    branch_principal = input("branch principal: ").strip()
    ling_programação = input("linguagem programação: ").strip()
    chave_SSH = input("chave SSH: ").strip()
    email = input("email: ").strip()
    status = input("Confirmar status (digite SUCESSO): ").strip().upper()

    # Validação direta com IF + AND
    if nickname_git.isalnum() and \
       nome_repositorio.isalnum() and \
        id_commit.isalnum() and \
       quant_linhas.isdigit() and \
       nome_desenvolvedor.isalpha() and \
        ling_programação.isalpha and \
        email.endswith("edu.br") and \
        len(chave_SSH) == 12 and \
        status == "SUCESSO":

       print(
            f"\nSUCESSO: cliente {nome_desenvolvedor}, "
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
