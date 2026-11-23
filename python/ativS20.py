print("---TERMINAL PONTUARIO---")
for tentativa in range(5):
    nome = input("Nome do motorist: ").strip()
    agencia = input("Qual o sobrenome?: ").strip()
    pais = input("Digitea cidade de saida:")
    nome_satelite= input("Digite a cidade de chegada: ").strip()
    transpoder= input("Digite a placa do caminhão: ").strip()
    altitude = input("Qual o chassi?: ").strip()
    velocidade = input("Qual o quilometragem?")
    frequencia = input ("Qual a capacidade do tanque?: ").strip()
    potência = input("Digite o codigo de carga: ").strip()
    pais_operador = input("Digite qual o pais operaor")
    data = input("Digite a data de viagem: ").strip()
    email = input ("Dgite o email da central:")
    alarme = input("Status:")

    if nome.isalpha() and\
    agencia.isalpha() and\
    pais.isalpha() and\
    nome_satelite.isalnum() and\
    transpoder.isalnum() and\
    altitude.isdigit() and\
    frequencia.isdigit() and\
    potência.isdigit() and\
    velocidade.isdigit() and\
    email.endswith(".space.org") and\
    len(transpoder) == 8 and \
    alarme == "CONFIRMADO":
      print(f"\nSUCESSO: o motorista de {nome}, com o {agencia} LIBERADO!") 
      break
    else:
       print(f"\nERRO:  Dados Inválidos! {tentativa + 1} de 5.")
       print("-"*40)
else:
   print("\nBLOQUEADO: Limite e 5 tentativas excedido. Procure o Diretor da Base.")
   