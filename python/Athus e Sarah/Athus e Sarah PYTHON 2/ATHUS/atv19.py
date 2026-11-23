print("-----Sistema de Controle de Contratos Futuros-----")

operador = input("Nome do Operador: ").strip()
corretora = input("Nome da Corretora: ").strip()
mercadoria = input("Mercadoria: ").strip()
cidade = input("Cidade da Bolsa: ").strip()
contrato = input("Código do Contrato: ").strip()
ordem = input("ID da Ordem de Compra: ").strip()
lotes = input("Quantidade de Lotes: ").strip()
margem = input("Margem de Garantia: ").strip()
data = input("Data do Contrato (DD/MM/AAAA): ").strip()
email = input("E-mail da Bolsa: ").strip()
chave = input("Chave Privada: ").strip()
status = input("Status (EXECUTADO): ").strip()

if operador.isalpha() and \
corretora.isalpha() and \
mercadoria.isalpha() and \
cidade.isalpha() and \
contrato.startswith("B3-") and contrato[3:].isalnum() and \
ordem.isalnum() and \
lotes.isdigit() and \
margem.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".b3.com.br") and \
chave.isalnum() and \
status == "EXECUTADO":

    print("Contrato executado!")
else:
    print("Dados inválidos!")

print("-" * 30)