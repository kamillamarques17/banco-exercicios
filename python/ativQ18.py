print("--- EXPORTAÇÃO DE CARNAS E FRIGORÍFICOS ---")
for tentativa in range(5):
    auditor = input("Nome do Auditor Sanitário: ").strip().title()
    empresa = input("Empresa Frigorífica: ").strip().title()
    corte = input("Tipo de Corte: ").strip().title()
    porto = input("Porto de Embarque: ").strip().title()
    container = input("Número do Container (Ex: REEFER-01): ").strip()
    certificado = input("Certificado Internacional: ").strip()
    temp = input("Temperatura de Congelamento: ").strip()
    peso = input("Peso Líquido em Quilos: ").strip()
    data = input("Data da Inspeção (DD-MM-AAAA): ").strip()
    email = input("E-mail do Ministério da Agricultura: ").strip().lower()
    lacre = input("Lacre Eletrônico: ").strip()
    parecer = input("Parecer de Exportação (LIBERADO): ").strip().upper()
    data_formatada = data.replace("-", "/")

    if auditor.isalpha() and \
       empresa.isalpha() and \
       corte.isalpha() and \
       porto.isalpha() and \
       container.startswith("REEFER-") and \
       certificado.isalnum() and \
       temp.isdigit() and \
       peso.isdigit() and \
       data_formatada.count("/") == 2 and \
       email.endswith(".mapa.gov.br") and \
       parecer == "LIBERADO":
        
        lacre_oculto = "*" * len(lacre)
        print(f"\nSUCESSO: Carga inspecionada por {auditor} no porto {porto}!")
        print(f"Data Padronizada: {data_formatada} | Lacre Protegido: {lacre_oculto}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas.")