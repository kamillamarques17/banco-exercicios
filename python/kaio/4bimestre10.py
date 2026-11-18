print("----------------Monitoramento Ambiental e Estação Meteorológica da Amazônia---------------------")

for tentativas in range(5):

    nome_pesquisador = input("Nome do pesquisador: ").strip()
    reserva_florestal = input("Digite a reserva florestal: ").strip()
    bioma_monitorado = input("Digite o bioma monitorado: ").strip()
    município_sensor = input("Digite o município do sensor: ").strip()
    codigo_estação = input("Digite o código da estação: ").strip().upper()
    modelo_pluvimento = input("Digite o modelo de pluvimento: ").strip()
    indice_uv = input("Digite o índice UV médio: ").strip()
    volume_chuva = input("Digite o volume de chuva em milímetros: ").strip()
    data = input("Data da coleta (DD/MM/AAAA): ").strip()
    email = input("E-mail do INPE: ").strip()
    chave_calibração = input("Digite a chave de calibração: ").strip()
    parecer = input("Parecer climático (VALIDO): ").strip().upper()

    if nome_pesquisador.isalpha() and \
       reserva_florestal.isalpha() and \
       bioma_monitorado.isalpha() and \
       município_sensor.isalpha() and \
       codigo_estação.startswith("DATA-") and codigo_estação[5:].isalnum() and \
       modelo_pluvimento.isalnum() and \
       indice_uv.isdigit() and \
       volume_chuva.isdigit() and \
       len(data) == 10 and data.count("/") == 2 and \
       email.count("@") == 1 and email.endswith(".inpe.gov.br") and \
       chave_calibração.isdigit() and \
       parecer == "VALIDO":

        print(f"\nSUCESSO: Pesquisador {nome_pesquisador}, Dados autorizados!")
        break

    else:
        print(f"\nERRO: Dados invalidos! {tentativas + 1} de 5")

else:
    print("\nAcesso negado")

print("-" * 40)