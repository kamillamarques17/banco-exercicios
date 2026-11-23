print("---Sistema de Lançamento Espacial---)")

for tentativa in range(5):
    #coletando e tratando os dados na entrada
    missao = input("Nome da Missão : ").strip()
    cod_foguete = input("Código do Foguete (EX: APOLLO11): ").strip().upper()
    data = input("Data do lançamento (DD/MM/AAAA): ").strip()
    id_astronauta= input("gital do Astronauta: ").strip()
    email_base = input("E-mail da Base: ").strip().lower()
    combustivel = input("Nível de Combustível (Apenas números): ").strip()
    carga = input("Carga espacial: ").strip()
    pressao = input ("Pressão da Cabine: ").strip()
    cidade = input("Cidade de Origem: ").strip()
    status = input("status do sistema (Digite APROVADO): ").strip().upper()

    #VALIDAÇÃO DIRETA COM IF + AND + QUEBRA DE LINHA (\)
    if cod_foguete.isalnum() and \
    carga.isalnum() and \
    id_astronauta.isdigit() and \
    combustivel.isdigit() and \
    pressao.isdigit() and \
    cidade.isalpha() and \
    email_base.endswith(".gov.br") and \
    len(data) == 10 and \
    status == "APROVADO": 

        print(f"\nSucesso: Astronauta {id_astronauta}, foguete {cod_foguete} liberado!")
        break
    else:
        #Exibe a tentativa amigavel (1 a 5)
        print(f"\nERRO: Dados invalidos! Tentativa{ tentativa + 1} de 5.") 
else:
    print("\nBLOQUEADO: Limite de 5 tentativas excedido. Procura o diretor da base.")
