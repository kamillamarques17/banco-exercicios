print("-------------Cadastro de Projeto de Engenharia-------------")

projeto = input("Nome do projeto:").strip()
codigo = input("Código do projeto:").strip()
engenheiro = input("Nome do engenheiro responsável:").strip()
crea = input("CREA do engenheiro responsável:").strip()
setor = input("Setor de atuação do projeto:").strip()
orcamento = input("Orçamento do projeto:").strip()
data_inicio = input("Data de início do projeto (DD/MM/AAAA):").strip()
data_fim = input("Data de término do projeto (DD/MM/AAAA):").strip()
uf = input("UF onde o projeto será executado:").strip()
cidade = input("Cidade onde o projeto será executado:").strip()
email_resp = input("E-mail do responsável pelo projeto:").strip()
cliente = input("Nome do cliente:").strip()
cnpj_cliente = input("CNPJ do cliente (somente números):").strip()
prioridade = input("Prioridade deve ser:").strip().upper()
status = input("Status:").strip()

if engenheiro.isalpha() and cidade.isalpha() and\
    crea.isdigit() and orcamento.isdigit() and cnpj_cliente.isdigit() and\
    projeto.upper() and setor.upper() and uf.upper() and status.upper() and\
    codigo.isalnum() and email_resp.count("@") == 1 and email_resp.endswith(".com") and\
    data_inicio.count("/") == 2 and len (data_inicio) ==10 and data_fim.count("/") == 2 and len (data_fim) ==10 and\
    status == "APROVADO":
    print(f"Sucesso: O projeto {projeto} foi cadastrado com sucesso!")
    
print("-"*60)