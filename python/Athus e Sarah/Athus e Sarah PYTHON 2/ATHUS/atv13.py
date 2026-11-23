print("-----Sistema de Monitoramento Ambiental-----")

pesquisador = input("Nome do Pesquisador: ").strip()
reserva = input("Reserva Florestal: ").strip()
bioma = input("Bioma: ").strip()
municipio = input("Município: ").strip()
estacao = input("Código da Estação: ").strip()
pluviometro = input("Modelo do Pluviômetro: ").strip()
uv = input("Índice UV: ").strip()
chuva = input("Índice de Chuva: ").strip()
data = input("Data da Medição (DD/MM/AAAA): ").strip()
email = input("E-mail do INPE: ").strip()
calibracao = input("Chave de Calibração: ").strip()
status = input("Status (VALIDADO): ").strip()

if pesquisador.isalpha() and \
reserva.isalpha() and \
bioma.isalpha() and \
municipio.isalpha() and \
estacao.startswith("MET-") and estacao[4:].isalnum() and \
pluviometro.isalnum() and \
uv.isdigit() and \
chuva.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".inpe.br") and \
calibracao.isalnum() and \
status == "VALIDADO":

    print("Medição validada!")
else:
    print("Dados inválidos!")

print("-" * 30)