print("-----Sistema de Controle de Aeroporto Militar-----")

oficial = input("Nome do Oficial: ").strip()
patente = input("Patente: ").strip()
esquadrao = input("Esquadrão: ").strip()
base = input("Cidade da Base: ").strip()
aeronave = input("Registro da Aeronave: ").strip()
missao = input("Código da Missão: ").strip()
combustivel = input("Nível de Combustível: ").strip()
teto = input("Teto de Voo: ").strip()
data = input("Data da Missão (DD/MM/AAAA): ").strip()
email = input("E-mail Militar: ").strip()
iff = input("Chave IFF: ").strip()
status = input("Status (AUTORIZADO): ").strip()

if oficial.isalpha() and \
patente.isalpha() and \
esquadrao.isalpha() and \
base.isalpha() and \
aeronave.isalnum() and \
missao.startswith("MISSAO-") and missao[7:].isalnum() and \
combustivel.isdigit() and \
teto.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".fab.mil.br") and \
iff.isalnum() and \
status == "AUTORIZADO":

    print("Missão autorizada!")
else:
    print("Dados inválidos!")

print("-" * 30)