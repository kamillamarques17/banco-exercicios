print("-----Centro Espacial e Telemetria de Satélites-----")

for tentativa in range(5):
    diretor = input("Nome do Diretor: ").strip().title()
    agencia = input("Agência Espacial: ").strip().title()
    satelite = input("Nome do Satélite: ").strip().upper()
    transponder = input("Código do Transponder: ").strip().upper()
    altitude = input("Altitude Orbital: ").strip()
    velocidade = input("Velocidade Orbital: ").strip()
    frequencia = input("Frequência de Uplink: ").strip()
    potencia = input("Potência dos Painéis: ").strip()
    pais = input("País Operador: ").strip().title()
    data = input("Data do Rastreio (DD/MM/AAAA): ").strip()
    email = input("E-mail do Centro de Controle: ").strip().lower()
    sinal = input("Sinal de Telemetria: ").strip().upper()

    if diretor.isalpha() and agencia.isalpha() and pais.isalpha() and \
       satelite.isalnum() and transponder.isalnum() and \
       altitude.isdigit() and velocidade.isdigit() and \
       frequencia.isdigit() and potencia.isdigit() and \
       len(transponder) == 8 and \
       len(data) == 10 and \
       email.endswith(".space.org") and \
       "@" in email and \
       sinal == "SINCRONIZADO":

        print(f"\nSUCESSO: Satélite {satelite} sincronizado!")
        print(f"Diretor: {diretor}")
        print(f"Data do Rastreio: {data}")
        print(f"Status: {sinal}")
        break

    else:
        print(f"\nERRO: Dados inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)

else:
    print("\nBLOQUEADO: Limite de 5 tentativas excedido.")
