print("--- EXTRAÇÃO DE PETRÓLEO OFFSHORE ---")
for tentativa in range(5):
    supervisor = input("Nome do Supervisor: ").strip().title()
    bacia = input("Bacia de Extração: ").strip().title()
    campo = input("Nome do Campo: ").strip().title()
    cidade = input("Cidade Portuária de Apoio: ").strip().title()
    poco = input("Código do Poço (Ex: POCO-01): ").strip()
    tag = input("Tag da Válvula Submarina: ").strip()
    pressao = input("Pressão no Cabeçote: ").strip()
    vazao = input("Vazão em Barris por Dia: ").strip()
    data = input("Data do Monitoramento (DD-MM-AAAA): ").strip()
    email = input("E-mail da Operadora: ").strip().lower()
    chave = input("Chave da Válvula de Emergência: ").strip()
    estado = input("Estado do Poço (ATIVO): ").strip().upper()
    data_formatada = data.replace("-", "/")

    if supervisor.isalpha() and \
       bacia.isalpha() and \
       campo.isalpha() and \
       cidade.isalpha() and \
       poco.startswith("POCO-") and \
       tag.isalnum() and \
       pressao.isdigit() and \
       vazao.isdigit() and \
       data_formatada.count("/") == 2 and \
       len(data_formatada) == 10 and \
       email.endswith(".oil.com.br") and \
       estado == "ATIVO":
        
        chave_oculta = "*" * len(chave)
        print(f"\nSUCESSO: Poço {poco} na bacia {bacia} monitorado por {supervisor}!")
        print(f"Data Padronizada: {data_formatada} | Chave Protegida: {chave_oculta}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas.")