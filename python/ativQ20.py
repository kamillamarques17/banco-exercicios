print("--- COMANDO AEROESPACIAL E DEFESA ANTIAÉREA ---")
for tentativa in range(5):
    comandante = input("Nome do Comandante de Operações: ").strip().title()
    forca = input("Força Armada: ").strip().title()
    bateria = input("Tipo de Bateria: ").strip().title()
    cidade = input("Cidade do Centro de Controle: ").strip().title()
    alvo = input("Código do Alvo (Ex: TARGET-01): ").strip()
    radar = input("Código do Radar Tridimensional: ").strip()
    distancia = input("Distância do Vetor em Km: ").strip()
    altitude = input("Altitude do Vetor em Metros: ").strip()
    data = input("Data do Rastreamento (DD-MM-AAAA): ").strip()
    email = input("E-mail do Ministério da Defesa: ").strip().lower()
    chave = input("Chave de Tiro Criptografada: ").strip()
    prontidao = input("Estado de Prontidão (PRONTO): ").strip().upper()
    data_formatada = data.replace("-", "/")

    if comandante.isalpha() and \
       forca.isalpha() and \
       bateria.isalpha() and \
       cidade.isalpha() and \
       alvo.startswith("TARGET-") and \
       radar.isalnum() and \
       distancia.isdigit() and \
       altitude.isdigit() and \
       data_formatada.count("/") == 2 and \
       len(data_formatada) == 10 and \
       email.endswith(".defesa.gov.br") and \
       prontidao == "PRONTO":
        
        chave_oculta = "*" * len(chave)
        print(f"\nSUCESSO: Alvo {alvo} rastreado pelo Comandante {comandante} ({forca})!")
        print(f"Data Padronizada: {data_formatada} | Chave de Tiro Protegida: {chave_oculta}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas. Notifique a Defesa Antiaérea.")