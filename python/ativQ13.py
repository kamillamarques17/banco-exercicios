print("--- MONITORAMENTO AMBIENTAL - AMAZÔNIA ---")
for tentativa in range(5):
    pesquisador = input("Nome do Pesquisador: ").strip().title()
    reserva = input("Reserva Florestal: ").strip().title()
    bioma = input("Bioma Monitorado: ").strip().title()
    municipio = input("Município do Sensor: ").strip().title()
    estacao = input("Código da Estação: ").strip()
    pluviometro = input("Modelo do Pluviômetro: ").strip()
    uv = input("Índice UV Medido: ").strip()
    chuva = input("Volume de Chuva em mm: ").strip()
    data = input("Data da Coleta (DD-MM-AAAA): ").strip()
    email = input("E-mail do INPE: ").strip().lower()
    chave = input("Chave de Calibração: ").strip()
    parecer = input("Parecer Climático (VALIDADO): ").strip().upper()
    data_formatada = data.replace("-", "/")

    if pesquisador.isalpha() and \
       reserva.isalpha() and \
       bioma.isalpha() and \
       municipio.isalpha() and \
       estacao.startswith("MET-") and \
       pluviometro.isalnum() and \
       uv.isdigit() and \
       chuva.isdigit() and \
       data_formatada.count("/") == 2 and \
       len(data_formatada) == 10 and \
       email.endswith(".inpe.br") and \
       parecer == "VALIDADO":
        
        chave_oculta = "*" * len(chave)
        print(f"\nSUCESSO: Dados coletados por {pesquisador} na reserva {reserva}!")
        print(f"Data Padronizada: {data_formatada} | Chave Protegida: {chave_oculta}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas.")