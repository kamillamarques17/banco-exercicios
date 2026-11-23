print("--- SUPERVISÓRIO DE USINA TERMELÉTRICA ---")
for tentativa in range(5):
    engenheiro = input("Nome do Engenheiro Chefe: ").strip().title()
    setor = input("Setor Operacional: ").strip().title()
    usina = input("Nome da Usina: ").strip().upper()
    cidade = input("Cidade da Instalação: ").strip().title()
    reator = input("Código do Reator : ").strip()
    tag = input("Tag da Turbina: ").strip()
    pressao = input("Pressão do Vapor: ").strip()
    rpm = input("Rotações por Minuto: ").strip()
    data = input("Data da Verificação (DD-MM-AAAA): ").strip()
    email = input("E-mail da Concessionária: ").strip().lower()
    chave = input("Chave de Bypass: ").strip()
    status = input("Status da Caldeira (NORMAL): ").strip().upper()
    data_formatada = data.replace("-", "/")

    if engenheiro.isalpha() and \
       setor.isalpha() and \
       cidade.isalpha() and \
       reator.startswith("TURB-") and \
       tag.isalnum() and \
       pressao.isdigit() and \
       rpm.isdigit() and \
       data_formatada.count("/") == 2 and \
       email.endswith(".energia.ind.br") and \
       status == "NORMAL":
        
        chave_oculta = "*" * len(chave)
        print(f"\nSUCESSO: Verificação realizada por {engenheiro} no setor {setor} da usina {usina}!")
        print(f"Data Padronizada: {data_formatada} | Chave Protegida: {chave_oculta}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas.")