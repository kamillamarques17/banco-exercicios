print("--- NOTIFICAÇÃO DE INFRAÇÕES DE TRÂNSITO ---")
for tentativa in range(5):
    condutor = input("Nome do Condutor: ").strip().title()
    sobrenome = input("Sobrenome: ").strip().title()
    bairro = input("Bairro da Infração: ").strip().title()
    municipio = input("Município do Registro: ").strip().title()
    placa = input("Placa do Veículo: ").strip()
    infracao = input("Código da Infração: ").strip()
    velocidade = input("Velocidade Aferida: ").strip()
    limite = input("Limite da Via: ").strip()
    data = input("Data do Auto (DD-MM-AAAA): ").strip()
    email = input("E-mail do DETRAN: ").strip().lower()
    radar = input("Código do Radar: ").strip()
    notificacao = input("Validação da Notificação (EMITIDO): ").strip().upper()
    data_formatada = data.replace("-", "/")

    if condutor.isalpha() and \
       sobrenome.isalpha() and \
       bairro.isalpha() and \
       municipio.isalpha() and \
       infracao.startswith("MULTA-") and \
       placa.isalnum() and \
       len(placa) == 7 and \
       velocidade.isdigit() and \
       limite.isdigit() and \
       data_formatada.count("/") == 2 and \
       email.endswith(".detran.gov.br") and \
       notificacao == "EMITIDO":
        
        radar_oculto = "*" * len(radar)
        print(f"\nSUCESSO: Notificação emitida para {condutor} {sobrenome} no município {municipio}!")
        print(f"Data Padronizada: {data_formatada} | Radar Protegido: {radar_oculto}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas.")