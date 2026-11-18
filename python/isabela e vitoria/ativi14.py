print("--- AUTOMAÇÃO INDUSTRIAL E SUPERVISÓRIO DE USINA HIDRELÉTRICA ---")

for tentativa in range(5):

    nome_operador = input("Nome do Operador: ").strip()
    turno = input("Turno de Trabalho: ").strip()
    sigla_turbina = input("Sigla da Turbina: ").strip()
    codigo_gerador = input("Código do Gerador: ").strip()
    rpm = input("Rotação (RPM): ").strip()
    nivel_represa = input("Nível da Represa: ").strip()
    vazao = input("Vazão da Água: ").strip()
    temperatura = input("Temperatura dos Mancais: ").strip()
    sala_comando = input("Sala de Comando: ").strip()
    data_leitura = input("Data da Leitura (DD/MM/AAAA): ").strip()
    email = input("E-mail da Usina: ").strip()
    alarme = input("Alarme Geral: ").strip()

    if nome_operador.isalpha() and \
       turno.isalpha() and \
       sala_comando.isalpha() and \
       sigla_turbina.isalnum() and \
       codigo_gerador.isalnum() and \
       rpm.isdigit() and \
       nivel_represa.isdigit() and \
       vazao.isdigit() and \
       temperatura.isdigit() and \
       len(data_leitura) == 10 and \
       email.endswith(".energia.ind.br") and \
       alarme == "NORMAL":

        print("\nSUCESSO: Leitura registrada com segurança!")
        print(f"Operador: {nome_operador}")
        print(f"Turno: {turno}")
        print(f"Sigla da Turbina: {sigla_turbina}")
        print(f"Código do Gerador: {codigo_gerador}")
        print(f"Rotação: {rpm} RPM")
        print(f"Nível da Represa: {nivel_represa}")
        print(f"Vazão da Água: {vazao}")
        print(f"Temperatura dos Mancais: {temperatura}")
        print(f"Sala de Comando: {sala_comando}")
        print(f"Data da Leitura: {data_leitura}")
        print(f"E-mail da Usina: {email}")
        print(f"Alarme Geral: {alarme}")
        break

    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)

else:
    print("\nBLOQUEADO: Limite de 5 tentativas atingido.")
    print("Contate o suporte técnico.")
