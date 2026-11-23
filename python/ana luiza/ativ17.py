print("---SISTEMA DE DEFESA---")
for tentativa in range(5):
    nome_analista = input("Nome do motorist: ").strip()
    equipe = input("Qual o sobrenome?: ").strip()
    cod_incidente = input("Digitea cidade de saida:")
    IP_origem= input("Digite a cidade de chegada: ").strip()
    IP_destino= input("Digite a placa do caminhão: ").strip()
    porta = input("Qual o chassi?: ").strip()
    tipo = input("Qual o quilometragem?")
    severidade = input ("Qual a capacidade do tanque?: ").strip()
    código = input("Digite o codigo de carga: ").strip()
    data = input("Digite a data de viagem: ").strip()
    email = input ("Dgite o email da central:")
    alarme = input("Status:")

    if nome_analista.isalpha() and\
    equipe.isalpha() and\
    tipo.isalpha() and\
    cod_incidente.isalpha() and\
    código.isalnum() and\
    IP_destino.isalnum() and\
    IP_origem.isalnum() and\
    porta.isdigit() and\
    severidade.isdigit() and\
    email.endswith(".soc.sec") and\
    len(cod_incidente) == 8 and \
    alarme == "MITIGADO":
      print(f"\nSUCESSO: o motorista de {nome_analista}, com o {cod_incidente} LIBERADO!") 
      break
    else:
       print(f"\nERRO:  Dados Inválidos! {tentativa + 1} de 5.")
       print("-"*40)
else:
   print("\nBLOQUEADO: Limite e 5 tentativas excedido. Procure o Diretor da Base.")
   