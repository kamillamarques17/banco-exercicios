print("---AUDITORIA---")
for tentativa in range(5):
    nome_auditor = input("Nome do auditor: ").strip()
    cargo = input("Qual o cargo da empresa?: ").strip()
    simbolo = input("Digite o simbolo do token:")
    cod_hash= input("Digite o codigo hash do bloco: ").strip()
    chave= input("Digite a chave publica: ").strip()
    taxa = input("Qual a taa o gas?: ").strip()
    quantidade = input("Qual a quantidade transferida?")
    numero = input ("Qual o numero de confirmação?: ").strip()
    pais = input("Digite o pais: ").strip()
    data = input("Digite a data da operação: ").strip()
    email = input ("Dgite o email:")
    parecer = input("Status:")

    if nome_auditor.isalpha() and\
    cargo.isalpha() and\
    pais.isalpha() and\
    simbolo.isalnum() and\
    chave.isalnum() and\
    cod_hash.isalnum() and\
    taxa.isdigit() and\
    quantidade.isdigit() and\
    numero.isdigit() and\
    email.endswith(".exchange.io") and\
    len(chave) == 12 and \
    parecer == "CONCLUIDO":
      print(f"\nSUCESSO: o auditor de nome {nome_auditor}, com o {cod_hash} LIBERADO!") 
      break
    else:
       print(f"\nERRO:  Dados Inválidos! {tentativa + 1} de 5.")
       print("-"*40)
else:
   print("\nBLOQUEADO: Limite e 5 tentativas excedido. Procure o Diretor da Base.")
   