print("-----Plataforma de Comércio Exterior e Importação Aduaneira-----")

importador = input("Nome do Importador: ").strip()
razao = input("Razão Social: ").strip()
origem = input("Porto de Origem: ").strip()
destino = input("Porto de Destino: ").strip()
container = input("Código do Container: ").strip()
declaracao = input("Número da Declaração: ").strip()
quantidade = input("Quantidade de Itens: ").strip()
peso = input("Peso Bruto: ").strip()
tarifario = input("Código Tarifário: ").strip()
data = input("Data do Despacho (DD/MM/AAAA): ").strip()
email = input("E-mail da Alfândega: ").strip()
parecer = input("Parecer Fiscal (LIBERADO): ").strip()

if importador.isalpha() and \
razao.isalpha() and \
origem.isalpha() and \
destino.isalpha() and \
container.isalnum() and \
tarifario.isalnum() and \
declaracao.isdigit() and \
quantidade.isdigit() and \
peso.isdigit() and \
email.count("@" == 1) and \
email.endswith(".gov.br") and \
len(data) == 10 and \
parecer == "LIBERADO":

    print("Importação liberada!")
else:
    print("Dados inválidos!")

print("-" * 30)