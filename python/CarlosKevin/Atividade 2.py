print ("---Registro de Criptoativo---")

for tentativa in range(5):
    #colentando e tartando os dados na entrada 
    cliente = input("Nome do cliente: ").strip()
    criptomoeda = input("Nome da Criptomoeda: ").strip()
    cod_hash = input("Data da Transação (DD/MM/AAAA): ").strip()
    Data = input("Código hash da carteira: ").strip() 
    id_bloco = input("ID númerico do bloco: ").strip()
    email = input("E-Mail de Suporte:").strip()
    quant_moedas = input("Quantidade de Moedas: ").strip()
    cod_taxa = input("Código da Taxa: ").strip()
    pais = input("País da Corretora: ").strip()
    autenticaçao = input("confirmar autenticaçao ( APROVADO) : ").strip().upper()

    #VALIDAÇAO DIRETA COM IF + QUEBRA DE LINHA (\)
    if criptomoeda.isalnum() and \
       cod_hash.isalnum() and \
       id_bloco.isdigit() and \
       quant_moedas.isdigit() and \
       pais.isalpha() and \
       email.endswith("crypto.com") and \
       email.count("@") == 2 and \
       len(Data) == 10 and\
       autenticaçao == "APROVADO":

        print(f"\nSUCESSO: Resgistro Aprovado {id_bloco}, foguete {cod_hash} liberado!")
        break
    else:
        #Exibe a tentativa amigavel (1 a 5)
        print(f"nERRO: Dados Ivalido! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEAO: Limite de 5 tentativas excedido. Procure o Corretora da Base.")