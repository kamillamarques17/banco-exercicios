print ("--- CADASTRO DE DESENVOLVIMENTO E REPOSITORIO GIT ---")

for tentativa in range(5):
    #colentando e tartando os dados na entrada 
    nome = input("Nome do Desenvolvidor: ").strip()
    nickname_git = input("Nickname Git: ").strip()
    nome_repositorio = input("Numero do Repositorio: ").strip()
    id_commit = input("ID do Commit: ").strip() 
    quant_linha = input("Quantidade de linhas: ").strip()
    branch_principal = input("Branch Principal: ").strip()
    linhagem = input("Linhagem de Programaçao: ").strip()
    chave_usuario = input("Chave SSH do Usuario: ").strip()
    email = input("E-mail Institucional: ").strip()
    status = input("Status do Deploy : ").strip()

    #VALIDAÇAO DIRETA COM IF + QUEBRA DE LINHA (\)
    if nickname_git.isalnum() and \
       id_commit.isalnum() and \
       nome_repositorio.isalnum() and \
       quant_linha.isdigit() and \
       nome.isalpha() and \
       linhagem.isalpha() and \
       len(chave_usuario) == 12 and \
       email.count("@") == 1 and email.endswith(".edu.br") and \
       status == "SUCESSO":

        print(f"\nSUCESSO: CADASTRO {nome}, REPOSITORIO {nome_repositorio} liberado!")
        break
    else:
        #Exibe a tentativa amigavel (1 a 5)
        print(f"nERRO: Dados Ivalido! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEAO: Limite de 5 tentativas excedido. Procure o Diretor da Base.")