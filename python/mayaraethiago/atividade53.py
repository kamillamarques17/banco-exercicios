print("--------CADASTRO DE PROJETO DE ENGENHARIA---------")
for tentativa in range(3):
    Projeto = input("Qual o projeto: ").strip()
    Código = input("nforme o código: ").strip()
    Engenheiro = input("Nome do engenheiro: ").strip()
    CREA = input("Digite o CREA: ").strip()
    Setor = input("Digite o setor: ").strip()
    Orçamento = input("Informe o orçamento da obra: ").strip()
    Data_Inicio = input("Data: (DD/MM/AAAA) ").strip()
    Data_Fim = input("Data: (DD/MM/AAAA) ").strip()
    Cidade = input("Informe a cidade: ").strip()
    Uf = input("Informe o UF: ").strip()
    Email_Resp = input("Informe o e-mail do responsavel: ").strip()
    Cliente = input("Nome do cliente: ").strip()
    CNPJ = input("CNPJ: ").strip()
    Prioridade = input("Qual a prioridade? ").strip()
    Status = input("Qual os status: ").strip().upper()

    if Engenheiro.isalpha() and Cidade.isalpha() and\
       CREA.isdigit() and Orçamento.isdigit() and CNPJ.isdigit() and Projeto.upper() and\
       Setor.upper() and Uf.upper() and Status.upper() and \
       Código.isalnum() and Email_Resp.count("@") == 1 and  Data_Inicio.count("/") == 2 and Data_Fim.count("/") and \
       Status == "APROVADO":
     
       print(f"SUCESSO: Cadastrado!")
       break
    else:
        print(f"ERRO: Tente novamente!.")
        print("-" * 40)
else:
    print("BLOQUEADO: Muitas falhas.")




