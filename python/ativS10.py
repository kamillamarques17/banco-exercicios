print("----CENTRO DE PESQUISA---")
for tentativa in range(5):
    nome_pesquisador = input("Nome do pesquisador: ").strip()
    sobrenome = input("Qual o sobrenome?: ").strip()
    cod_reator = input("Digite o código do reator:")
    setor_acesso = input("Digite o setor de acesso: ").strip()
    nível_radiação= input("Digite o nível e radiação: ").strip()
    Data_inspeção = input("Data de inspeção (DD/MM/AAAA): ").strip()
    cartão_aces = input ("Qual o cartão de acesso?: ").strip()
    id = input("Digite o id: ").strip()
    temperatura = input("Digite a temperatura do nucleo: ").strip()
    cid_lab = input("Cidade do laboratorio: ").strip()
    email_const = input ("Dgite o email constitucional:").strip()
    segurança = input("Status:").strip()

    if nome_pesquisador.isalpha() and\
    sobrenome.isalpha() and\
    setor_acesso.isalpha() and\
    cid_lab.isalpha() and\
    cod_reator.isalnum() and\
    cartão_aces.isalnum() and\
    nível_radiação.isdigit() and\
    id.isdigit() and\
    temperatura.isdigit() and\
    email_const.count("@") and email_const.endswith(".gov.br") and\
    len(Data_inspeção) == 10 and \
    segurança == "APROVADO":
      print(f"\nSUCESSO: o pequisador de {nome_pesquisador}, com o cartão {cartão_aces} APROVADO!") 
      break
    else:
       print(f"\nERRO:  Dados Inválidos! {tentativa + 1} de 5.")
       print("-"*40)
else:
   print("\nBLOQUEADO: Limite e 5 tentativas excedido. Procure o Diretor da Base.")
   