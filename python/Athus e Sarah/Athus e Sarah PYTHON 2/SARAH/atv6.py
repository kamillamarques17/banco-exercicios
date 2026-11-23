print("-----Sistema de Transporte Ferroviário-----")

maquinista = input("Nome do Maquinista: ").strip()
origem = input("Terminal de Origem: ").strip()
destino = input("Terminal de Destino: ").strip()
minerio = input("Tipo de Minério: ").strip()
vagao = input("Código do Vagão: ").strip()
trem = input("Número do Trem: ").strip()
peso = input("Peso da Carga: ").strip()
distancia = input("Distância em Quilômetros: ").strip()
data = input("Data do Transporte (DD/MM/AAAA): ").strip()
email = input("E-mail Ferroviário: ").strip()
freio = input("Chave do Freio: ").strip()
status = input("Status (VERDE): ").strip()

if maquinista.isalpha() and \
origem.isalpha() and \
destino.isalpha() and \
minerio.isalpha() and \
vagao.startswith("CARGA-") and vagao[6:].isalnum() and \
trem.isalnum() and \
peso.isdigit() and \
distancia.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".ferrovia.log.br") and \
freio.isalnum() and \
status == "VERDE":

    print("Transporte autorizado!")
else:
    print("Dados inválidos!")

print("-" * 30)