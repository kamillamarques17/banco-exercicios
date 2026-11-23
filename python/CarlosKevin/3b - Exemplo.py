print ("--- SISTEMA DE LANÇAMENTO ESPACIAL---")

for tentativa in range(5):
    #colentando e tartando os dados na entrada 
    missao = input("Nome da Missao: ").strip()
    cod_foguete = input("Codigo do foguete (Ex:APOLLO11): ").strip().upper()
    data = input("Data do Lançamento (DD/MM/AAAA): ").strip()
    id_astronauta = input("ID Digital do Astronauta: ").strip() 
    email_base = input("E-mail da Base: ").strip().lower()
    combustivel = input("Nivel de Combustivel (Apenas numeros): ").strip()
    carga = input("Carga Espacial: ").strip()
    pressao = input("Pressao de Cabine: ").strip()
    cidade = input("Cidade de Origem: ").strip()
    status = input("Status do Sistema (Digite APROVADO) : ").strip().upper()

    #VALIDAÇAO DIRETA COM IF + QUEBRA DE LINHA (\)
    if cod_foguete.isalnum() and \
       carga.isalnum() and \
       id_astronauta.isdigit() and \
       combustivel.isdigit() and \
       pressao.isdigit() and \
       cidade.isalpha() and \
       email_base.endswith(".gov.br") and \
       status == "APROVADO":

        print(f"\nSUCESSO: Astronauta {id_astronauta}, foguete {cod_foguete} liberado!")
        break
    else:
        #Exibe a tentativa amigavel (1 a 5)
        print(f"nERRO: Dados Ivalido! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEAO: Limite de 5 tentativas excedido. Procure o Diretor da Base.")