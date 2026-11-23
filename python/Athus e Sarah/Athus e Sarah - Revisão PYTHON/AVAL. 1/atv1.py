print("-----Controle de Acesso ao Centro de Pesquisa Nuclear-----")

nome = input("Nome do Pesquisador: ").strip()
sobrenome = input("Sobrenome: ").strip()
reator = input("Código do Reator: ").strip()
setor = input("Setor de Acesso: ").strip()
radiacao = input("Nível de Radiação: ").strip()
data = input("Data da Inspeção (DD/MM/AAAA): ").strip()
cartao = input("Cartão de Acesso: ").strip()
cracha = input("ID do Crachá: ").strip()
temperatura = input("Temperatura do Núcleo: ").strip()
cidade = input("Cidade do Laboratório: ").strip()
email = input("E-mail Institucional: ").strip()
status = input("Status de Segurança (APROVADO): ").strip()

if nome.isalpha() and \
sobrenome.isalpha() and \
setor.isalpha() and \
cidade.isalpha() and \
reator.isalnum() and \
cartao.isalnum() and \
radiacao.isdigit() and \
cracha.isdigit() and \
temperatura.isdigit() and \
email.count("@" == 1) and \
email.endswith(".gov.br") and \
len(data) == 10 and \
status == "APROVADO":

    print("Acesso aprovado!")
else:
    print("Dados inválidos!")

print("-" * 30)