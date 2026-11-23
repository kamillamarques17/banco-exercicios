print("-----Sistema de Registro de Multas de Trânsito-----")

motorista = input("Nome do Motorista: ").strip()
sobrenome = input("Sobrenome: ").strip()
bairro = input("Bairro: ").strip()
municipio = input("Município: ").strip()
placa = input("Placa do Veículo: ").strip()
infracao = input("Código da Infração: ").strip()
velocidade = input("Velocidade Registrada: ").strip()
limite = input("Limite de Velocidade: ").strip()
data = input("Data da Infração (DD/MM/AAAA): ").strip()
email = input("E-mail do DETRAN: ").strip()
radar = input("Código do Radar: ").strip()
status = input("Status (EMITIDO): ").strip()

if motorista.isalpha() and \
sobrenome.isalpha() and \
bairro.isalpha() and \
municipio.isalpha() and \
placa.isalnum() and len(placa) == 7 and \
infracao.startswith("MULTA-") and infracao[6:].isalnum() and \
velocidade.isdigit() and \
limite.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".detran.gov.br") and \
radar.isalnum() and \
status == "EMITIDO":

    print("Multa emitida!")
else:
    print("Dados inválidos!")

print("-" * 30)