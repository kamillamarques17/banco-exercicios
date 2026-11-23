print("---DESPACHO DE CARGAS---")
for tentativa in range(5):
    nome_motorista = input("Nome do motorista: ").strip()
    cid_destino = input("qual cidade?: ").strip()
    placa = input("Digite a placa:")
    cod_rastreamento = input("Digite o codigo de rastresmenti: ").strip()
    peso_kg= input("Digite o peso da carga: ").strip()
    num_fis = input("Digite o numero da nota fiscal: ").strip()
    email = input ("Qual o email?: ").strip()
    tipo_transporte = input("Digite o tipo de transporte: ").strip()
    CEP = input("Digite o CEP de entrega: ").strip()
    Confirmação = input("Status: ").strip()

    if nome_motorista.isalpha() and\
    cid_destino.isalpha() and\
    tipo_transporte.isalpha() and\
    placa.isalnum and\
    cod_rastreamento.isalnum() and\
    peso_kg.isdigit() and\
    num_fis.isdigit() and\
    CEP.isdigit() and\
    email.endswith(".log.br") and\
    len(CEP) == 8 and \
    Confirmação == "AUTORIZADO":
      print(f"\nSUCESSO: Motorista de {nome_motorista}, com o codigo {cod_rastreamento} AUTORIZADO!") 
      break
    else:
       print(f"\nERRO:  Dados Inválidos! {tentativa + 1} de 5.")
       print("-"*40)
else:
   print("\nBLOQUEADO: Limite e 5 tentativas excedido. Procure o Diretor da Base.")
   