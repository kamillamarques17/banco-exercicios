print("--- CONTROLE DE IMIGRAÇÃO E PASSAPORTES ---")
for tentativa in range(5):
    passageiro = input("Nome do Passageiro: ").strip().title()
    sobrenome = input("Sobrenome: ").strip().title()
    pais = input("País de Origem: ").strip().title()
    cidade = input("Cidade de Destino: ").strip().title()
    passaporte = input("Número do Passaporte: ").strip()
    voo = input("Código do Voo (Ex: FLIGHT-123): ").strip()
    bagagens = input("Quantidade de Bagagens: ").strip()
    dias = input("Tempo de Estadia em Dias: ").strip()
    data = input("Data de Entrada (DD-MM-AAAA): ").strip()
    email = input("E-mail da Companhia Aérea: ").strip().lower()
    visto = input("Código de Visto: ").strip()
    entrada = input("Entrada no País (AUTORIZADO): ").strip().upper()
    data_formatada = data.replace("-", "/")

    if passageiro.isalpha() and \
       sobrenome.isalpha() and \
       pais.isalpha() and \
       cidade.isalpha() and \
       voo.startswith("FLIGHT-") and \
       passaporte.isalnum() and \
       len(passaporte) == 8 and \
       bagagens.isdigit() and \
       dias.isdigit() and \
       data_formatada.count("/") == 2 and \
       email.endswith(".air.com") and \
       entrada == "AUTORIZADO":
        
        visto_oculto = "*" * len(visto)
        print(f"\nSUCESSO: Passageiro {passageiro} {sobrenome} do país {pais} autorizado!")
        print(f"Data Padronizada: {data_formatada} | Visto Protegido: {visto_oculto}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas.")