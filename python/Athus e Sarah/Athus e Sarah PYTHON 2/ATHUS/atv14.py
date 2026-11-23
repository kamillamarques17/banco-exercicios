print("-----Sistema de Fabricação Farmacêutica-----")

farmaceutico = input("Nome do Farmacêutico: ").strip()
ingrediente = input("Ingrediente Ativo: ").strip()
forma = input("Forma Farmacêutica: ").strip()
cidade = input("Cidade: ").strip()
lote = input("Código do Lote: ").strip()
anvisa = input("Registro ANVISA: ").strip()
quantidade = input("Quantidade de Comprimidos: ").strip()
dosagem = input("Dosagem em mg: ").strip()
data = input("Data de Fabricação (DD/MM/AAAA): ").strip()
email = input("E-mail Farmacêutico: ").strip()
hash = input("Hash da Fórmula: ").strip()
status = input("Status (APROVADO): ").strip()

if farmaceutico.isalpha() and \
ingrediente.isalpha() and \
forma.isalpha() and \
cidade.isalpha() and \
lote.startswith("LOTE-") and lote[5:].isalnum() and \
anvisa.isalnum() and \
quantidade.isdigit() and \
dosagem.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".pharma.ind.br") and \
hash.isalnum() and \
status == "APROVADO":

    print("Fabricação aprovada!")
else:
    print("Dados inválidos!")

print("-" * 30)