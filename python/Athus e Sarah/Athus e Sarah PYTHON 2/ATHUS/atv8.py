print("-----Sistema de Leilão de Gado-----")

pecuarista = input("Nome do Pecuarista: ").strip()
fazenda = input("Nome da Fazenda: ").strip()
raca = input("Raça do Animal: ").strip()
municipio = input("Município: ").strip()
brinco = input("Brinco Eletrônico: ").strip()
genealogia = input("Registro Genealógico: ").strip()
peso = input("Peso em Arrobas: ").strip()
idade = input("Idade em Meses: ").strip()
data = input("Data do Leilão (DD/MM/AAAA): ").strip()
email = input("E-mail Agropecuário: ").strip()
pin = input("PIN de Segurança: ").strip()
status = input("Status (APROVADO): ").strip()

if pecuarista.isalpha() and \
fazenda.isalpha() and \
raca.isalpha() and \
municipio.isalpha() and \
brinco.startswith("BOV-") and brinco[4:].isalnum() and \
genealogia.isalnum() and \
peso.isdigit() and \
idade.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".agro.org.br") and \
pin.isdigit() and \
status == "APROVADO":

    print("Animal aprovado para o leilão!")
else:
    print("Dados inválidos!")

print("-" * 30)