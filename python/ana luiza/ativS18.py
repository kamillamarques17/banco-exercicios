print("---TERMINAL PONTUARIO---")
for tentativa in range(5):
    nome_pratico = input("Nome do motorist: ").strip()
    pais = input("Qual o sobrenome?: ").strip()
    nome_navio = input("Digitea cidade de saida:")
    código= input("Digite a cidade de chegada: ").strip()
    calado= input("Digite a placa do caminhão: ").strip()
    numero = input("Qual o chassi?: ").strip()
    tonelagem = input("Qual o quilometragem?")
    cod_rebocador = input ("Qual a capacidade do tanque?: ").strip()
    canal = input("Digite o codigo de carga: ").strip()
    data = input("Digite a data de viagem: ").strip()
    email = input ("Dgite o email da central:")
    alarme = input("Status:")

    if nome_pratico.isalpha() and\
    nome_navio.isalpha() and\
    pais.isalpha() and\
    cod_rebocador.isalnum() and\
    código.isalnum() and\
    canal.isalnum() and\
    calado.isdigit() and\
    numero.isdigit() and\
    tonelagem.isdigit() and\
    email.endswith(".marinha.mil.br") and\
    len(código) == 7 and \
    alarme == "CONFIRMADO":
      print(f"\nSUCESSO: o motorista de {nome_pratico}, com o {cod_rebocador} LIBERADO!") 
      break
    else:
       print(f"\nERRO:  Dados Inválidos! {tentativa + 1} de 5.")
       print("-"*40)
else:
   print("\nBLOQUEADO: Limite e 5 tentativas excedido. Procure o Diretor da Base.")
   