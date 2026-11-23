print("-----Terminal Portuário e Controle de Atracação Marítima-----")

for tentativa in range(5):
    pratico = input("Nome do Prático: ").strip()
    pais = input("País da Embarcação: ").strip()
    navio = input("Nome do Navio: ").strip()
    imo = input("Código IMO: ").strip()
    calado = input("Calado do Navio: ").strip()
    berco = input("Número do Berço: ").strip()
    tonelagem = input("Tonelagem da Carga: ").strip()
    rebocador = input("Código do Rebocador: ").strip()
    canal = input("Canal de Atracação: ").strip()
    data = input("Data da Atracação (DD/MM/AAAA): ").strip()
    email = input("E-mail da Capitania: ").strip().lower()
    autorizacao = input("Autorização Portuária: ").strip().upper()

    if pratico.isalpha() and pais.isalpha() and navio.isalpha() and \
       imo.isalnum() and rebocador.isalnum() and canal.isalnum() and \
       calado.isdigit() and berco.isdigit() and tonelagem.isdigit() and \
       len(imo) == 7 and len(data) == 10 and \
       email.endswith(".marinha.mil.br") and \
       "@" in email and \
       autorizacao == "CONFIRMADO":

        print(f"\nSUCESSO: navio {navio} autorizado.")
        break

    else:
        print(f"\nERRO: cadastro inválido, Tentativa {tentativa + 1} de 5")
        print("-" * 40)

else:
    print("\nBLOQUEADO: Limite de 5 tentativas excedido.")
