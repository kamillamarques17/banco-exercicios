print("---IMPORTAÇÃO ADUANEIRA---")
for tentativa in range(5):
    nome_portador = input("Nome do portador: ").strip()
    razao = input("Qual a razão social?: ").strip()
    porta_origem = input("Digite a porta e origem:")
    porto__destino = input("Digite o porto de destino: ").strip()
    cod_container= input("Digite o codigo do container: ").strip()
    num_declaração = input("Qual o numero da declaração:): ").strip()
    quantidade = input ("Quantidade?: ").strip()
    peso_bruto = input("Digite o peso bruto: ").strip()
    cod_tarifa = input("Digite o codigo do tarifaço: ").strip()
    data = input("Digite a data  do  despacho: ").strip()
    email_alfandega = input ("Dgite o email da alfandega:")
    parecer_fiscal = input("Status:")

    if nome_portador.isalpha() and\
    razao.isalpha() and\
    porta_origem.isalpha() and\
    porto__destino.isalpha() and\
    cod_container.isalnum() and\
    cod_tarifa.isalnum() and\
    num_declaração.isdigit() and\
    quantidade.isdigit() and\
    peso_bruto.isdigit() and\
    email_alfandega.count("@") and email_alfandega.endswith(".gov.br") and\
    len(data) == 10 and \
    parecer_fiscal == "LIBERADO":
      print(f"\nSUCESSO: o portador de {nome_portador}, com  razõ social {razao} LIBERADO!") 
      break
    else:
       print(f"\nERRO:  Dados Inválidos! {tentativa + 1} de 5.")
       print("-"*40)
else:
   print("\nBLOQUEADO: Limite e 5 tentativas excedido. Procure o Diretor da Base.")
   