print("---CADASTRO GERAL---")
for tentativa in range(5):
    nome = input("Nome do motorist: ").strip()
    sobrenome= input("Qual o sobrenome?: ").strip()
    bairro = input("Digitea cidade de saida:")
    cid_registro= input("Digite a cidade de chegada: ").strip()
    num = input("Digite a placa do caminhão: ").strip()
    cod_IPTU = input("Qual o chassi?: ").strip()
    area = input("Qual o quilometragem?")
    valor = input ("Qual a capacidade do tanque?: ").strip()
    numero = input("Digite o codigo de carga: ").strip()
    data = input("Digite a data de viagem: ").strip()
    email = input ("Dgite o email da central:")
    alarme = input("Status:")

    if nome.isalpha() and\
    sobrenome.isalpha() and\
    bairro.isalpha() and\
    cid_registro.isalpha() and\
    num.isalnum() and\
    cod_IPTU.isalnum() and\
    area.isdigit() and\
    numero.isdigit() and\
    valor.isdigit() and\
    email.endswith(".cartorio.not.br") and\
    len(data) == 10 and \
    alarme == "REGISTRADO":
      print(f"\nSUCESSO: o motorista de {nome}, com o {sobrenome} LIBERADO!") 
      break
    else:
       print(f"\nERRO:  Dados Inválidos! {tentativa + 1} de 5.")
       print("-"*40)
else:
   print("\nBLOQUEADO: Limite e 5 tentativas excedido. Procure o Diretor da Base.")
   