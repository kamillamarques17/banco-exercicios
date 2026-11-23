print ("--- CONTROLE DE LOGISTICA E DESPACHO DE CARGA ---")

for tentativa in range(5):
    #colentando e tartando os dados na entrada 
    nome = input("Nome do Desenvolvidor: ").strip()
    cidade = input("Nickname Git: ").strip()
    placa_veiculo = input("Numero do Repositorio: ").strip()
    codigo = input("ID do Commit: ").strip() 
    peso_quilo = input("Quantidade de linhas: ").strip()
    nota_fiscal = input("Branch Principal: ").strip()
    transpote = input("Linhagem de Programaçao: ").strip()
    email = input("Chave SSH do Usuario: ").strip()
    cep = input("E-mail Institucional: ").strip()
    status = input("Status do Deploy : ").strip()

    #VALIDAÇAO DIRETA COM IF + QUEBRA DE LINHA (\)
    if nome.isalnum() and \
       cidade.isalnum() and \
       transpote.isalnum() and \
       placa_veiculo.isdigit() and \
       codigo.isalpha() and \
       peso_quilo.isalpha() and \
       nota_fiscal == 12 and \
       email.count("@") == 1 and email.endswith(".edu.br") and \
       status == "SUCESSO":

        print(f"\nSUCESSO: CADASTRO {nome}, REPOSITORIO {cidade} liberado!")
        break
    else:
        #Exibe a tentativa amigavel (1 a 5)
        print(f"nERRO: Dados Ivalido! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEAO: Limite de 5 tentativas excedido. Procure o Diretor da Base.")