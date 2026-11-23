print("---GESTÃO DE FROTA---")
for tentativa in range(5):
    nome_operador = input("Nome do motorist: ").strip()
    turno = input("Qual o sobrenome?: ").strip()
    sigla = input("Digitea cidade de saida:")
    cod_gerador= input("Digite a cidade de chegada: ").strip()
    rotação= input("Digite a placa do caminhão: ").strip()
    nivel = input("Qual o chassi?: ").strip()
    vazao = input("Qual o quilometragem?")
    temperatura = input ("Qual a capacidade do tanque?: ").strip()
    sala = input("Digite o codigo de carga: ").strip()
    data = input("Digite a data de viagem: ").strip()
    email = input ("Dgite o email da central:")
    alarme = input("Status:")

    if nome_operador.isalpha() and\
    turno.isalpha() and\
    sigla.isalpha() and\
    cod_gerador.isalpha() and\
    rotação.isalnum() and\
    nivel.isalnum() and\
    vazao.isalnum() and\
    temperatura.isdigit() and\
    sala.isdigit() and\
    email.endswith(".tranporte.comisalnum") and\
    len(data) == 10 and \
    alarme == "NORMAL":
      print(f"\nSUCESSO: o motorista de {nome_operador}, com o {cod_gerador} LIBERADO!") 
      break
    else:
       print(f"\nERRO:  Dados Inválidos! {tentativa + 1} de 5.")
       print("-"*40)
else:
   print("\nBLOQUEADO: Limite e 5 tentativas excedido. Procure o Diretor da Base.")
   