print("---GESTÃO DE FROTA---")
for tentativa in range(5):
    nome_motorista = input("Nome do motorist: ").strip()
    sobrenome = input("Qual o sobrenome?: ").strip()
    cid_saida = input("Digitea cidade de saida:")
    cid_chegada= input("Digite a cidade de chegada: ").strip()
    placa= input("Digite a placa do caminhão: ").strip()
    chassi = input("Qual o chassi?: ").strip()
    quilometragem = input("Qual o quilometragem?")
    capacidade = input ("Qual a capacidade do tanque?: ").strip()
    cod_carga = input("Digite o codigo de carga: ").strip()
    data = input("Digite a data de viagem: ").strip()
    email = input ("Dgite o email da central:")
    autorização = input("Status:")

    if nome_motorista.isalpha() and\
    sobrenome.isalpha() and\
    cid_saida.isalpha() and\
    cid_chegada.isalpha() and\
    placa.isalnum() and\
    chassi.isalnum() and\
    cod_carga.isalnum() and\
    quilometragem.isdigit() and\
    capacidade.isdigit() and\
    email.endswith(".tranporte.comisalnum") and\
    len(placa) == 7 and \
    autorização == "AUTORIZADO":
      print(f"\nSUCESSO: o motorista de {nome_motorista}, com o {cod_carga} LIBERADO!") 
      break
    else:
       print(f"\nERRO:  Dados Inválidos! {tentativa + 1} de 5.")
       print("-"*40)
else:
   print("\nBLOQUEADO: Limite e 5 tentativas excedido. Procure o Diretor da Base.")
   