print("--- GESTÃO DE TRÁFEGO FERROVIÁRIO ---")
for tentativa in range(5):
    maquinista = input("Nome do Maquinista: ").strip().title()
    partida = input("Terminal de Partida: ").strip().title()
    chegada = input("Terminal de Chegada: ").strip().title()
    minerio = input("Tipo de Minério: ").strip().title()
    vagao = input("Código do Vagão: ").strip()
    trem = input("Número do Trem: ").strip()
    peso = input("Peso em Toneladas: ").strip()
    km = input("Quilômetros a Percorrer: ").strip()
    data = input("Data da Viagem (DD-MM-AAAA): ").strip()
    email = input("E-mail da Ferrovia: ").strip().lower()
    chave = input("Chave do Bloqueio de Freio: ").strip()
    sinalizacao = input("Sinalização da Linha (VERDE): ").strip().upper()
    data_formatada = data.replace("-", "/")

    if maquinista.isalpha() and \
       partida.isalpha() and \
       chegada.isalpha() and \
       minerio.isalpha() and \
       vagao.startswith("CARGA-") and \
       trem.isalnum() and \
       peso.isdigit() and \
       km.isdigit() and \
       data_formatada.count("/") == 2 and \
       len(data_formatada) == 10 and \
       email.endswith(".ferrovia.log.br") and \
       sinalizacao == "VERDE":
        
        chave_oculta = "*" * len(chave)
        print(f"\nSUCESSO: Trem {trem} conduzido por {maquinista} liberado!")
        print(f"Data Padronizada: {data_formatada} | Chave Protegida: {chave_oculta}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas.")