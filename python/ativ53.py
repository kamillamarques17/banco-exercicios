print("----------------CADASTRO DE PROJETO DE ENGENHARIA--------------")
for tentativa in range(3):
    projeto = input("Qual o projeto:").strip()
    código = input("Informe o código:").strip()
    engenharia = input ("Nome do engenheiro:").strip()
    CREA = input ("Digite o CREA:").strip()
    setor = input("Digite o setor:").strip()
    orçamento = input("Infrome o orçmneto da obra:").strip()
    data_inicio = input("Data: (DD/MM/AAAA): ").strip()
    data_fim = input("Data: (DD/MM/AAAA):").strip()
    cidade = input("Informe a cidade: ").strip()
    uf = input("Informe o Uf:").strip()
    email_resp = input("Informe o e-mial do responsavel:").strip()
    cliente = input("Nome do cliente: ").strip()
    CNPJ = input("CNPJ:").strip()
    prioridade = input("Qual a prioridade:").strip()
    status = input("Qual o status?: ").strip().upper()

    if engenharia.isalpha() and cidade.isalpha() and\
    CREA.isdigit() and orçamento.isdigit() and CNPJ.isdigit() and projeto.upper() and\
    setor.upper() and uf.upper() and status.upper() and\
    código.isalnum() and email_resp.count("@") == 1 and data_inicio.count("/") == 2 and data_fim.count("/") and\
    status == "APROVADO":
        print(f"SUCESSO: Cadastro!")
        break
    else:
        print(F"ERRO: Tente novamente!")
        print("-"*40)

else:
    print("BLOQUEADO: Muitas falhas.")