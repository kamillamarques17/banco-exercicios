print('----------Cadastro de Projeto de Engenharia----------')

projeto = input("Nome do projeto: ").strip()
codigo = input("Código do projeto: ").strip()
engenheiro = input("Nome do engenheiro responsável: ").strip()
crea = input("CREA do engenheiro responsável (Núm.): ").strip()
setor = input("Setor: ").strip()
orcamento = input("Estipule o orçamento (Núm.): ").strip()
data_inicio = input("Digite a data de início (Núm.): ").strip()
data_final = input("Digite a data final (Núm.): ").strip()
uf = input("UF: ").strip()
cidade = input("Cidade: ").strip()
email_resp = input("E-mail do responsável: ").strip()
cliente = input("Nome do cliente: ").strip()
cnpj_cliente = input("CNPJ do cliente: ").strip()
prioridade = input("Prioridade deve ser: ").strip()
status = input("Status: ").strip()

if engenheiro.isalpha() and cidade.isalpha() and \
crea.isdigit() and orcamento.isdigit() and cnpj_cliente.isdigit() and \
projeto.upper() and setor.upper() and uf.upper() and status.upper() and \
codigo.isalnum() and email_resp.count("@") == 1 and email_resp.endswith(".com") and \
data_inicio.count("/") == 2 and len(data_inicio) == 10 and data_final.count("/") == 2 and len(data_final) == 10 and \
status == "APROVADO":
     print("Cadastrado com sucesso!")

print('-' * 50)