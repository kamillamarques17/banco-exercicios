print("---Sistema de lançamento espacial---")

for tentativa in range(5):
    #Coleta e tratando os dados na entrada
    missao = input("Nome da missão: ").strip()
    cod_foguete = input("codigo do foguete (EX: APOLLO011):").strip().upper()
    data = input("Data do lançamento (DD/MM/AAAA):").strip()
    id_astronauta = ("ID Digite do astronauta: ").strip()
    email_base = input("E-mail da base: ").strip().lower()
    Combustivel = input("Nivel de combustivel (Apenas números):").strip()
    Carga = input("carga Espacial: ").strip()
    pressão = input("pressao da cabine: ").strip()
    cidade = input("Cidade de Origem: ").strip()
    status = input("Status do sistema (Digite APROVADO): ").strip().upper()

    # VALIDAÇÃO DIRETA COM IF + AND + QUEBRA DE LONHA (\)
    if cod_foguete.isalnum() and \
       Carga.isalnum() and \
       id_astronauta.isdigit() and \
       Combustivel.isdigit() and \
       pressão.isdigit() and \
       cidade.isalpha() and \
       email_base.endswith(".gov.br") and \
       len(data) == 10 and \
       status == "APROVADO":

       print(f"\nSucesso: Astronauta {id_astronauta}, foguete {cod_foguete} liberado!")
       break
    else:
        #Exige a tentativas amigavel (1 a 5)
        print(f"\nErro: Dados invalidos! Tentavi {tavtativas +1} de 5.")
        print("-"* 40)
else:
        print("\nBLOQUEADO: Limite de 5 tantativas excedido. procure o Diretor da base.")